import { defineStore } from "pinia"
import { getDashboardResults } from "../api/dashboard.api"

export const useDashboardStore = defineStore("dashboard", {
  state: () => ({
    totals: {
      income: 0,
      expense: 0,
    },
    monthlySummary: {},
    bankName: "-",
    totalTransactions: 0,
    manualAdjustment: 0,

    // ✅ CATEGORY DATA (SAFE DEFAULTS)
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
    netCashFlowWithManual(state) {
      return this.netCashFlow + Number(state.manualAdjustment)
    },
  },

  actions: {
    async fetchDashboardData(jobId) {
      if (this.loading || this.loaded) return

      this.loading = true
      this.error = null

      try {
        const response = await getDashboardResults(jobId)
        const data = response.data ?? response

        // ===== TOTALS =====
        this.totals.income = Number(data?.totals?.credit ?? 0)
        this.totals.expense = Number(data?.totals?.debit ?? 0)

        // ===== MONTHLY =====
        const mappedMonthly = {}
        for (const [month, values] of Object.entries(data?.monthly_summary ?? {})) {
          mappedMonthly[month] = {
            income: Number(values.credit ?? 0),
            expense: Number(values.debit ?? 0),
          }
        }
        this.monthlySummary = mappedMonthly

        this.bankName = data?.bank_name ?? "-"
        this.totalTransactions = Number(data?.total_transactions ?? 0)
        this.manualAdjustment = Number(data?.manual_adjustment ?? 0)

        // 🔥 CATEGORY SUMMARY MAPPING
        const categorySummary = data?.category_summary || {}

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
              : 0
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
      this.monthlySummary = {}
      this.bankName = "-"
      this.totalTransactions = 0
      this.manualAdjustment = 0

      this.incomeCategories = []
      this.expenseCategories = []
      this.uncategorizedAmount = 0

      this.loaded = false
      this.loading = false
      this.error = null
    },
  },
})
