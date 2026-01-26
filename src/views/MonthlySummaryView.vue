<template>
<div class="min-h-screen px-4 md:px-10 pt-5 md:pt-8 pb-8 text-slate-200 bg-transparent">
  <!-- Header -->
    <div class="mb-8 flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
  <!-- Title -->
  <div>
    <h1 class="text-2xl font-semibold text-white">
      Monthly Financial Summary
    </h1>
    <p class="text-slate-400 mt-1">
      Month-wise income, expenses, and net cash flow
    </p>
    <p class="text-sm text-slate-500 mt-1">
      Generated from processed bank statement
    </p>
  </div>

  <!-- TOGGLE -->
  <div
  class="inline-flex w-full md:w-[220px] shrink-0
         rounded-full bg-slate-800/70 border border-white/10 p-1"
>

      <button
        @click="viewMode = 'table'"
        class="flex-1 py-2 text-sm font-medium rounded-full transition text-center"
        :class="
          viewMode === 'table'
            ? 'bg-indigo-500/20 text-indigo-400'
            : 'text-slate-400 hover:text-white'
        "
      >
        Table
      </button>

      <button
        @click="viewMode = 'cards'"
        class="flex-1 py-2 text-sm font-medium rounded-full transition text-center"
        :class="
          viewMode === 'cards'
            ? 'bg-indigo-500/20 text-indigo-400'
            : 'text-slate-400 hover:text-white'
        "
      >
        Cards
      </button>

  </div>
</div>


    <!-- TABLE VIEW (Desktop) -->
    <div
      v-if="viewMode === 'table'"
      class="bg-slate-800 border border-white/10 rounded-xl mb-8"
    >
      <div class="overflow-x-auto">
        <table class="min-w-[640px] w-full">

        <thead class="bg-slate-700/50 text-slate-300 text-sm">
          <tr>
            <th class="px-4 py-3 text-left text-sm font-semibold">Month</th>
            <th class="px-4 py-3 text-left text-sm font-semibold">Total Income</th>
            <th class="px-4 py-3 text-left text-sm font-semibold">Total Expenses</th>
            <th class="px-4 py-3 text-left text-sm font-semibold">Net Cash Flow</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="item in data"
            :key="item.month"
            class="border-t border-white/5 hover:bg-white/5 transition-all duration-200 group"
          >
            <!-- Month -->
            <td class="px-4 py-4 font-medium text-white whitespace-nowrap">
              {{ item.month }}
            </td>

            <!-- Total Income -->
            <td class="px-4 py-4 text-slate-300 whitespace-nowrap text-right">
              ₹{{ format(item.income) }}
            </td>

            <!-- Total Expenses -->
            <td class="px-4 py-4 text-slate-300 whitespace-nowrap text-right">
              ₹{{ format(item.expenses) }}
            </td>

            <!-- Net Cash Flow (UNCHANGED) -->
            <td class="px-6 py-4 text-right">
              <div class="flex items-center justify-end gap-2">
                <span
                  class="font-semibold text-lg"
                  :class="item.net >= 0 ? 'text-green-400' : 'text-sky-400'"
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
                  class="w-4 h-4 text-blue-600"
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
    </div>

    <!-- CARD VIEW -->
    <div
  v-if="viewMode === 'cards'"
  class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6"
>
      <div
        v-for="item in data"
        :key="item.month + '-card'"
        class="bg-slate-800 rounded-xl shadow-md p-6 border border-white/10
               hover:bg-slate-700/70 hover:-translate-y-1"
      >
        <h3 class="font-semibold text-lg mb-4 text-white">
          {{ item.month }}
        </h3>

        <div class="space-y-3">
          <div class="flex justify-between">
            <span class="text-slate-400">Income</span>
            <span class="font-semibold">₹{{ format(item.income) }}</span>
          </div>

          <div class="flex justify-between">
            <span class="text-slate-400">Expenses</span>
            <span class="font-semibold">₹{{ format(item.expenses) }}</span>
          </div>

          <div class="pt-3 border-t">
            <div class="flex justify-between items-center">
              <span class="font-semibold">Net Cash Flow</span>
              <div class="flex items-center gap-2">
                <span
                  class="font-bold"
                  :class="item.net >= 0 ? 'text-green-400' : 'text-sky-400'"
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
                  class="w-4 h-4 text-blue-600"
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
      class="mt-10 bg-slate-800/60 border border-white/10 rounded-lg p-4 text-sm text-slate-300 text-center"
    >
      Monthly values are generated by the system using verified transaction data.
      Totals match bank statement records.
    </div>

    <!-- FOOTER (UPDATED – ONLY CHANGE) -->
    <div class="mt-8 pt-4 border-t text-center text-xs text-slate-400 space-y-1">
      <p>By default, your data is processed in memory and discarded.</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const viewMode = ref('table') // 'table' | 'cards'

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
