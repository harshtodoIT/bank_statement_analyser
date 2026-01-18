<script setup>
  import { computed } from "vue";
  import { useDashboardStore } from "../../stores/dashboard.store";
  import CategoryDonut from "./CategoryDonut.vue";

  const store = useDashboardStore();

  const incomeTotal = computed(() =>
    store.totals.income || 0
  );

  const expenseTotal = computed(() =>
    store.totals.expense || 0
  );

  const netBalance = computed(() =>
    store.netCashFlow || 0
  );
  </script>

  <template>
    <div class="flex flex-col items-center space-y-10">

      <CategoryDonut />

      <div class="flex gap-6 text-sm">
        <div class="flex items-center gap-2">
          <span class="w-3 h-3 rounded-full bg-green-500"></span>
          <span>Income</span>
        </div>
        <div class="flex items-center gap-2">
          <span class="w-3 h-3 rounded-full bg-red-500"></span>
          <span>Expenses</span>
        </div>
        <div class="flex items-center gap-2">
          <span class="w-3 h-3 rounded-full bg-orange-500"></span>
          <span>Uncategorized</span>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 w-full">
        <div class="bg-green-50 border border-green-200 rounded-xl p-5">
          <p class="text-green-700 font-medium">Total Income</p>
          <p class="text-2xl font-semibold text-green-700">
            ₹{{ incomeTotal.toLocaleString() }}
          </p>
        </div>

        <div class="bg-red-50 border border-red-200 rounded-xl p-5">
          <p class="text-red-700 font-medium">Total Expenses</p>
          <p class="text-2xl font-semibold text-red-700">
            ₹{{ expenseTotal.toLocaleString() }}
          </p>
        </div>

        <div class="bg-blue-50 border border-blue-200 rounded-xl p-5">
          <p class="text-blue-700 font-medium">Net Balance</p>
          <p class="text-2xl font-semibold text-blue-700">
            ₹{{ netBalance.toLocaleString() }}
          </p>
        </div>
      </div>

    </div>
  </template>
