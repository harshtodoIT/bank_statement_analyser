<script setup>
  import { computed } from "vue";
  import { useDashboardStore } from "../stores/dashboard.store";

  const store = useDashboardStore();

  /**
   * Convert monthlySummary object into an ordered array
   * {
   *   "2024-04": { income, expense, net }
   * }
   * →
   * [
   *   { month: "Apr 2024", income, expenses, net }
   * ]
   */
  const data = computed(() => {
    return Object.entries(store.monthlySummary || {})
      .sort(([a], [b]) => a.localeCompare(b)) // chronological order
      .map(([monthKey, values]) => {
        const [year, month] = monthKey.split("-");
        const date = new Date(year, month - 1);

        return {
          month: date.toLocaleString("en-IN", {
            month: "short",
            year: "numeric"
          }),
          income: values.income,
          expenses: values.expense,
          net: values.net
        };
      });
  });

  const format = (num) =>
    new Intl.NumberFormat("en-IN").format(num);
  </script>

  <template>
    <div class="bg-gray-50 min-h-screen px-4 md:px-10 py-8">
      <!-- Header -->
      <div class="mb-8">
        <h1 class="text-3xl font-bold text-gray-900">
          Monthly Financial Summary
        </h1>
        <p class="text-gray-600 mt-1">
          Month-wise income, expenses, and net cash flow
        </p>
        <p class="text-sm text-gray-500 mt-1">
          Generated from processed bank statement
        </p>
      </div>

      <!-- TABLE VIEW (Desktop) -->
      <div
        class="hidden md:block bg-white rounded-xl shadow-lg overflow-hidden mb-8"
      >
        <table class="w-full">
          <thead class="bg-gray-100 text-gray-700 text-sm">
            <tr>
              <th class="px-6 py-4 text-left font-semibold">Month</th>
              <th class="px-6 py-4 text-right font-semibold">Total Income</th>
              <th class="px-6 py-4 text-right font-semibold">Total Expenses</th>
              <th class="px-6 py-4 text-right font-semibold">Net Cash Flow</th>
            </tr>
          </thead>

          <tbody>
            <tr
              v-for="item in data"
              :key="item.month"
              class="border-t hover:bg-gray-50 transition-all duration-200"
            >
              <td class="px-6 py-4 font-medium text-gray-900">
                {{ item.month }}
              </td>
              <td class="px-6 py-4 text-right">
                ₹{{ format(item.income) }}
              </td>
              <td class="px-6 py-4 text-right">
                ₹{{ format(item.expenses) }}
              </td>
              <td class="px-6 py-4 text-right">
                <span
                  class="font-semibold"
                  :class="item.net >= 0 ? 'text-green-600' : 'text-red-600'"
                >
                  {{ item.net < 0 ? "-" : "" }}₹{{ format(Math.abs(item.net)) }}
                </span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- CARD VIEW -->
      <div
        class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6"
      >
        <div
          v-for="item in data"
          :key="item.month + '-card'"
          class="bg-white rounded-xl shadow-md p-6 border border-gray-100
                 hover:shadow-xl hover:-translate-y-1 transition-all duration-300"
        >
          <h3 class="font-semibold text-lg mb-4 text-gray-900">
            {{ item.month }}
          </h3>

          <div class="space-y-3">
            <div class="flex justify-between">
              <span class="text-gray-600">Income</span>
              <span class="font-semibold">
                ₹{{ format(item.income) }}
              </span>
            </div>

            <div class="flex justify-between">
              <span class="text-gray-600">Expenses</span>
              <span class="font-semibold">
                ₹{{ format(item.expenses) }}
              </span>
            </div>

            <div class="pt-3 border-t flex justify-between">
              <span class="font-semibold">Net Cash Flow</span>
              <span
                class="font-bold"
                :class="item.net >= 0 ? 'text-green-600' : 'text-red-600'"
              >
                {{ item.net < 0 ? "-" : "" }}₹{{ format(Math.abs(item.net)) }}
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- INFO BOX -->
      <div
        class="mt-10 bg-blue-50 border border-blue-200 rounded-lg p-4
               text-sm text-gray-700 text-center"
      >
        Monthly values are generated using verified transaction data.
        Totals match bank statement records.
      </div>

      <!-- FOOTER -->
      <div
        class="mt-8 pt-4 border-t text-center text-xs text-gray-500 space-y-1"
      >
        <p>By default, your data is processed in memory and discarded.</p>
        <p class="font-medium">
          Monthly Summary Module – Designed & owned by Indra Kumar
        </p>
      </div>
    </div>
  </template>
