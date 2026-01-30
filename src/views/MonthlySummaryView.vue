<script setup>
import { ref, computed } from "vue"
import { useDashboardStore } from "../stores/dashboard.store"

const store = useDashboardStore()

// view toggle
const viewMode = ref("table") // 'table' | 'cards'

/**
 * Convert monthlySummary object into ordered array
 * ✅ USE BACKEND-PROVIDED net VALUE
 */
const data = computed(() => {
  return Object.entries(store.monthlySummary || {})
    .sort(([a], [b]) => a.localeCompare(b))
    .map(([monthKey, values]) => {
      const [year, month] = monthKey.split("-")
      const date = new Date(year, month - 1)

      return {
        month: date.toLocaleString("en-IN", {
          month: "short",
          year: "numeric"
        }),
        income: Number(values.income ?? 0),
        expenses: Number(values.expense ?? 0),
        net: Number(values.net ?? 0), // ✅ FIX
      }
    })
})

const format = (num) =>
  new Intl.NumberFormat("en-IN").format(num)
</script>

<template>
  <div class="min-h-screen px-4 md:px-10 pt-5 md:pt-8 pb-8 text-slate-200 bg-transparent">

    <!-- HEADER + TOGGLE -->
    <div class="mb-8 flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
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

      <!-- VIEW TOGGLE -->
      <div
        class="inline-flex w-full md:w-[220px]
               rounded-full bg-slate-800/70 border border-white/10 p-1"
      >
        <button
          @click="viewMode = 'table'"
          class="flex-1 py-2 text-sm font-medium rounded-full transition"
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
          class="flex-1 py-2 text-sm font-medium rounded-full transition"
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

    <!-- TABLE VIEW -->
    <div
      v-if="viewMode === 'table'"
      class="bg-slate-800 border border-white/10 rounded-xl mb-8"
    >
      <div class="overflow-x-auto">
        <table class="min-w-[640px] w-full">
          <thead class="bg-slate-700/50 text-slate-300 text-sm">
            <tr>
              <th class="px-4 py-3 text-left font-semibold">Month</th>
              <th class="px-4 py-3 text-right font-semibold">Total Income</th>
              <th class="px-4 py-3 text-right font-semibold">Total Expenses</th>
              <th class="px-4 py-3 text-right font-semibold">Net Cash Flow</th>
            </tr>
          </thead>

          <tbody>
            <tr
              v-for="item in data"
              :key="item.month"
              class="border-t border-white/5 hover:bg-white/5 transition"
            >
              <td class="px-4 py-4 font-medium text-white">
                {{ item.month }}
              </td>

              <td class="px-4 py-4 text-right">
                ₹{{ format(item.income) }}
              </td>

              <td class="px-4 py-4 text-right">
                ₹{{ format(item.expenses) }}
              </td>

              <td class="px-4 py-4 text-right">
                <span
                  class="font-semibold"
                  :class="item.net >= 0 ? 'text-green-400' : 'text-sky-400'"
                >
                  {{ item.net < 0 ? '-' : '' }}₹{{ format(Math.abs(item.net)) }}
                </span>
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
        class="bg-slate-800 rounded-xl p-6 border border-white/10
               hover:bg-slate-700/70 transition"
      >
        <h3 class="font-semibold text-lg mb-4 text-white">
          {{ item.month }}
        </h3>

        <div class="space-y-3">
          <div class="flex justify-between">
            <span class="text-slate-400">Income</span>
            <span class="font-semibold">
              ₹{{ format(item.income) }}
            </span>
          </div>

          <div class="flex justify-between">
            <span class="text-slate-400">Expenses</span>
            <span class="font-semibold">
              ₹{{ format(item.expenses) }}
            </span>
          </div>

          <div class="pt-3 border-t border-white/10 flex justify-between">
            <span class="font-semibold">Net Cash Flow</span>
            <span
              class="font-bold"
              :class="item.net >= 0 ? 'text-green-400' : 'text-sky-400'"
            >
              {{ item.net < 0 ? '-' : '' }}₹{{ format(Math.abs(item.net)) }}
            </span>
          </div>
        </div>
      </div>
    </div>

    <!-- INFO -->
    <div
      class="mt-10 bg-slate-800/60 border border-white/10 rounded-lg
             p-4 text-sm text-slate-300 text-center"
    >
      Monthly values are generated using verified transaction data.
      Totals match bank statement records.
    </div>

    <!-- FOOTER -->
    <div class="mt-8 pt-4 border-t border-white/10 text-center text-xs text-slate-400">
      By default, your data is processed in memory and discarded.
    </div>

  </div>
</template>
