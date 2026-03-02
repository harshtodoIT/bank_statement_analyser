import { defineStore } from "pinia"
import { getDashboardResults } from "../api/dashboard.api"

export const useDashboardStore = defineStore("dashboard", {
  state: () => ({
    totals: {
      income: 0,
      expense: 0,
    },

    // authoritative values
    netCashFlowWithManual: 0,
    manualAdjustments: [],

    monthlySummary: {},
    bankName: "-",
    totalTransactions: 0,

    // categories
    incomeCategories: [],
    expenseCategories: [],
    uncategorizedAmount: 0,

    loaded: false,
    loading: false,
    error: null,
  }),

  getters: {
    netCashFlow(state) {
      return Number(state.totals.income) - Number(state.totals.expense)
    },
  },

  actions: {
    async fetchDashboardData(jobId) {
      // 🛑 HARD GUARD — THIS FIXES EVERYTHING
      if (!jobId) {
        this.reset()
        return
      }

      if (this.loading) return

      this.loading = true
      this.error = null

      try {
        const response = await getDashboardResults(jobId)

        // normalize backend shape
        const payload = response?.data?.data ?? response?.data ?? response

        // totals
        this.totals.income = Number(payload?.totals?.credit ?? 0)
        this.totals.expense = Number(payload?.totals?.debit ?? 0)

        // net cash flow (manual-aware)
        this.netCashFlowWithManual = Number(
          payload?.net_cash_flow_with_manual ??
          payload?.net_cash_flow ??
          (this.totals.income - this.totals.expense)
        )

        this.manualAdjustments = payload?.manual_adjustments ?? []

        // monthly summary (derive net safely)
        const mappedMonthly = {}
        for (const [month, values] of Object.entries(payload?.monthly_summary ?? {})) {
          const income = Number(values.credit ?? 0)
          const expense = Number(values.debit ?? 0)

          mappedMonthly[month] = {
            income,
            expense,
            net: income - expense,
          }
        }
        this.monthlySummary = mappedMonthly

        this.bankName =
          payload?.bank_name && payload.bank_name.trim()
            ? payload.bank_name
            : "-"

        this.totalTransactions = Number(payload?.total_transactions ?? 0)

        // categories
        const categorySummary = payload?.category_summary ?? {}

        this.incomeCategories = []
        this.expenseCategories = []
        this.uncategorizedAmount = 0

        const totalExpense = Object.entries(categorySummary)
          .filter(([k]) => k !== "Income")
          .reduce((s, [, v]) => s + Number(v), 0)

        for (const [category, amount] of Object.entries(categorySummary)) {
          if (category === "Income") continue

          if (category === "Uncategorized") {
            this.uncategorizedAmount = Number(amount)
            continue
          }

          this.expenseCategories.push({
            name: category,
            amount: Number(amount),
            percent: totalExpense
              ? Math.round((Number(amount) / totalExpense) * 100)
              : 0,
          })
        }

        this.loaded = true
      } catch (err) {
        console.error("Dashboard fetch failed", err)
        this.error = "Failed to load dashboard data"
        this.loaded = false
      } finally {
        this.loading = false
      }
    },

    reset() {
      this.totals = { income: 0, expense: 0 }
      this.netCashFlowWithManual = 0
      this.manualAdjustments = []
      this.monthlySummary = {}
      this.bankName = "-"
      this.totalTransactions = 0

      this.incomeCategories = []
      this.expenseCategories = []
      this.uncategorizedAmount = 0

      this.loaded = false
      this.loading = false
      this.error = null
    },
  },
})
