import { defineStore } from "pinia";
import { getDashboardResults } from "../api/dashboard.api";
import { useProcessingStore } from "./processing.store";

export const useDashboardStore = defineStore("dashboard", {
  state: () => ({
    loading: false,
    error: null,

    totals: {
      income: 0,
      expense: 0
    },
    monthlySummary: {},
    categorySummary: {},
    manualAdjustments: [],
    netCashFlow: 0,
    netCashFlowWithManual: 0,

    // ✅ NEW
    totalTransactions: 0,
    bankName: "-",

    incomeCategories: [],
    expenseCategories: [],
    uncategorizedAmount: 0,
  }),

  actions: {
    async fetchDashboardData() {
      const processingStore = useProcessingStore();
      if (!processingStore.jobId) return;

      this.loading = true;
      this.error = null;

      try {
        const res = await getDashboardResults(processingStore.jobId);

        if (res.status === "FAILED") {
          this.error = res.error;
          return;
        }

        const data = res.data;

        this.totals = {
          income: data.totals.credit,
          expense: data.totals.debit
        };

        const normalizedMonthly = {};
        Object.entries(data.monthly_summary || {}).forEach(
          ([month, values]) => {
            normalizedMonthly[month] = {
              income: values.credit,
              expense: values.debit,
              net: values.net
            };
          }
        );

        this.monthlySummary = normalizedMonthly;
        this.categorySummary = data.category_summary;
        this.manualAdjustments = data.manual_adjustments;
        this.netCashFlow = data.net_cash_flow;
        this.netCashFlowWithManual = data.net_cash_flow_with_manual;

        // --- CATEGORY BREAKDOWN NORMALIZATION ---
        this.categorySummary = data.category_summary || {};

        this.incomeCategories = [];
        this.expenseCategories = [];
        this.uncategorizedAmount = 0;

        Object.entries(this.categorySummary).forEach(([name, amount]) => {
          if (name === "Income") {
            this.incomeCategories.push({ name, amount });
          } else if (name === "Uncategorized") {
            this.uncategorizedAmount = amount;
          } else {
            this.expenseCategories.push({ name, amount });
          }
        });


        // ✅ FIXED
        this.totalTransactions = data.total_transactions;
        this.bankName = data.bank_name;

      } catch {
        this.error = "Failed to load dashboard data";
      } finally {
        this.loading = false;
      }
    }
  }
});
