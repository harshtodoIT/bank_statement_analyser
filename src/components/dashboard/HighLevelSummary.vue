<script setup>
  import { computed } from "vue";
  import { useDashboardStore } from "../../stores/dashboard.store";

  const dashboardStore = useDashboardStore();

  const transactionCount = computed(() => {
    return dashboardStore.totalTransactions;
  });

  const dateRange = computed(() => {
    const months = Object.keys(dashboardStore.monthlySummary || {});
    if (!months.length) return "-";
    return `${months[0]} – ${months[months.length - 1]}`;
  });

  const bankName = computed(() => {
    return dashboardStore.bankName || "-";
  });
  </script>

  <template>
    <div class="bg-white rounded-2xl p-6 shadow-sm h-full">
      <h2 class="text-lg font-semibold text-gray-900 mb-6">
        High-Level Summary
      </h2>

      <div class="space-y-6">

        <div class="flex items-start gap-4">
          <div class="w-10 h-10 rounded-xl bg-blue-100 flex items-center justify-center">₹</div>
          <div>
            <p class="text-sm text-gray-500">Total Transactions Processed</p>
            <p class="text-lg font-semibold text-gray-900">
              {{ transactionCount }}
            </p>
          </div>
        </div>

        <div class="flex items-start gap-4">
          <div class="w-10 h-10 rounded-xl bg-blue-100 flex items-center justify-center">📅</div>
          <div>
            <p class="text-sm text-gray-500">Statement Date Range</p>
            <p class="text-lg font-semibold text-gray-900">
              {{ dateRange }}
            </p>
          </div>
        </div>

        <div class="flex items-start gap-4">
          <div class="w-10 h-10 rounded-xl bg-blue-100 flex items-center justify-center">🏦</div>
          <div>
            <p class="text-sm text-gray-500">Bank Detected</p>
            <p class="text-lg font-semibold text-gray-900">
              {{ bankName }}
            </p>
          </div>
        </div>

      </div>
    </div>
  </template>
