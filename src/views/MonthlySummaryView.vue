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
    <div class="hidden md:block bg-white rounded-xl shadow-lg overflow-hidden mb-8">
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
            class="border-t hover:bg-gray-50 transition-all duration-200 group"
          >
            <td class="px-6 py-4 font-medium text-gray-900">
              {{ item.month }}
            </td>
            <td class="px-6 py-4 text-right text-gray-700">
              ₹{{ format(item.income) }}
            </td>
            <td class="px-6 py-4 text-right text-gray-700">
              ₹{{ format(item.expenses) }}
            </td>
            <td class="px-6 py-4 text-right">
              <div class="flex items-center justify-end gap-2">
                <span
                  class="font-semibold text-lg"
                  :class="item.net >= 0 ? 'text-green-600' : 'text-red-600'"
                >
                  {{ item.net < 0 ? '-' : '' }}₹{{ format(Math.abs(item.net)) }}
                </span>

                <!-- POSITIVE ARROW -->
                <svg
                  v-if="item.net >= 0"
                  class="w-4 h-4 text-green-600"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  viewBox="0 0 24 24"
                >
                  <line x1="6" y1="18" x2="18" y2="6" />
                  <polyline points="12 6 18 6 18 12" />
                </svg>

                <!-- NEGATIVE ARROW -->
                <svg
                  v-else
                  class="w-4 h-4 text-red-600"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  viewBox="0 0 24 24"
                >
                  <line x1="6" y1="6" x2="18" y2="18" />
                  <polyline points="12 18 18 18 18 12" />
                </svg>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- CARD VIEW -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
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
            <span class="font-semibold">₹{{ format(item.income) }}</span>
          </div>

          <div class="flex justify-between">
            <span class="text-gray-600">Expenses</span>
            <span class="font-semibold">₹{{ format(item.expenses) }}</span>
          </div>

          <div class="pt-3 border-t">
            <div class="flex justify-between items-center">
              <span class="font-semibold">Net Cash Flow</span>
              <div class="flex items-center gap-2">
                <span
                  class="font-bold"
                  :class="item.net >= 0 ? 'text-green-600' : 'text-red-600'"
                >
                  {{ item.net < 0 ? '-' : '' }}₹{{ format(Math.abs(item.net)) }}
                </span>

                <!-- POSITIVE ARROW -->
                <svg
                  v-if="item.net >= 0"
                  class="w-4 h-4 text-green-600"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  viewBox="0 0 24 24"
                >
                  <line x1="6" y1="18" x2="18" y2="6" />
                  <polyline points="12 6 18 6 18 12" />
                </svg>

                <!-- NEGATIVE ARROW -->
                <svg
                  v-else
                  class="w-4 h-4 text-red-600"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  viewBox="0 0 24 24"
                >
                  <line x1="6" y1="6" x2="18" y2="18" />
                  <polyline points="12 18 18 18 18 12" />
                </svg>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- INFO BOX (same as Figma) -->
    <div
      class="mt-10 bg-blue-50 border border-blue-200 rounded-lg p-4 text-sm text-gray-700 text-center"
    >
      Monthly values are generated by the system using verified transaction data.
      Totals match bank statement records.
    </div>

    <!-- FOOTER (UPDATED – ONLY CHANGE) -->
    <div class="mt-8 pt-4 border-t text-center text-xs text-gray-500 space-y-1">
      <p>By default, your data is processed in memory and discarded.</p>
      <p class="font-medium">
        Monthly Summary Module – Designed &amp; owned by Indra Kumar
      </p>
    </div>
  </div>
</template>

<script setup>
const data = [
  { month: 'Jan 2024', income: 450000, expenses: 320000, net: 130000 },
  { month: 'Feb 2024', income: 380000, expenses: 410000, net: -30000 },
  { month: 'Mar 2024', income: 520000, expenses: 295000, net: 225000 },
  { month: 'Apr 2024', income: 410000, expenses: 385000, net: 25000 },
  { month: 'May 2024', income: 490000, expenses: 360000, net: 130000 },
  { month: 'Jun 2024', income: 445000, expenses: 420000, net: 25000 },
  { month: 'Jul 2024', income: 510000, expenses: 340000, net: 170000 },
  { month: 'Aug 2024', income: 395000, expenses: 450000, net: -55000 },
  { month: 'Sep 2024', income: 475000, expenses: 315000, net: 160000 },
  { month: 'Oct 2024', income: 530000, expenses: 390000, net: 140000 },
  { month: 'Nov 2024', income: 460000, expenses: 405000, net: 55000 },
  { month: 'Dec 2024', income: 485000, expenses: 375000, net: 110000 }
]

const format = (num) =>
  new Intl.NumberFormat('en-IN').format(num)
</script>
