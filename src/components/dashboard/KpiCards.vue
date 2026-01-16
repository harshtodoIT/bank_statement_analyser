<script setup>
  import { useDashboardStore } from "../../stores/dashboard.store";
  const dashboardStore = useDashboardStore();
  </script>

  <template>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">

      <div class="bg-white rounded-2xl p-6 shadow-sm relative">
        <div class="absolute right-3 top-6 h-12 w-1 bg-green-500 rounded"></div>
        <p class="text-sm text-gray-500">Total Income</p>
        <p class="text-3xl font-semibold text-green-600">
          ₹{{ dashboardStore.totals.income.toFixed(2) }}
        </p>
      </div>

      <div class="bg-white rounded-2xl p-6 shadow-sm relative">
        <div class="absolute right-3 top-6 h-12 w-1 bg-red-500 rounded"></div>
        <p class="text-sm text-gray-500">Total Expenses</p>
        <p class="text-3xl font-semibold text-red-600">
          ₹{{ dashboardStore.totals.expense.toFixed(2) }}
        </p>
      </div>

      <div class="bg-white rounded-2xl p-6 shadow-sm relative">
        <div class="absolute right-3 top-6 h-12 w-1 bg-blue-500 rounded"></div>
        <p class="text-sm text-gray-500">Net Cash Flow</p>
        <p class="text-3xl font-semibold text-blue-600">
          ₹{{ dashboardStore.netCashFlowWithManual.toFixed(2) }}
        </p>
      </div>

    </div>
  </template>
