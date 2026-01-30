<script setup>
import { computed } from "vue"
import { useDashboardStore } from "../../stores/dashboard.store"

import {
  IndianRupee,
  Calendar,
  Building2
} from "lucide-vue-next"

const dashboardStore = useDashboardStore()

// ✅ SAFE COMPUTEDS
const transactionCount = computed(() => {
  return dashboardStore.totalTransactions ?? 0
})

const dateRange = computed(() => {
  const summary = dashboardStore.monthlySummary ?? {}
  const months = Object.keys(summary)
  if (!months.length) return "-"
  return `${months[0]} – ${months[months.length - 1]}`
})

const bankName = computed(() => {
  return dashboardStore.bankName ?? "-"
})
</script>

<template>
  <div class="bg-slate-800 rounded-2xl p-6 border border-white/5 h-full">

    <h2 class="text-lg font-semibold text-white mb-6">
      High-Level Summary
    </h2>

    <div class="divide-y divide-white/5">

      <!-- Total Transactions -->
      <div class="flex items-start gap-4 py-4">
        <div class="w-10 h-10 rounded-xl bg-blue-500/20 flex items-center justify-center">
          <IndianRupee class="w-5 h-5 text-blue-400" />
        </div>
        <div>
          <p class="text-sm text-slate-400">
            Total Transactions Processed
          </p>
          <p class="text-lg font-semibold text-white">
            {{ transactionCount }}
          </p>
        </div>
      </div>

      <!-- Date Range -->
      <div class="flex items-start gap-4 py-4">
        <div class="w-10 h-10 rounded-xl bg-blue-500/20 flex items-center justify-center">
          <Calendar class="w-5 h-5 text-blue-400" />
        </div>
        <div>
          <p class="text-sm text-slate-400">
            Statement Date Range
          </p>
          <p class="text-lg font-semibold text-white">
            {{ dateRange }}
          </p>
        </div>
      </div>

      <!-- Bank -->
      <div class="flex items-start gap-4 py-4">
        <div class="w-10 h-10 rounded-xl bg-blue-500/20 flex items-center justify-center">
          <Building2 class="w-5 h-5 text-blue-400" />
        </div>
        <div>
          <p class="text-sm text-slate-400">
            Bank Detected
          </p>
          <p class="text-lg font-semibold text-white">
            {{ bankName }}
          </p>
        </div>
      </div>

    </div>

  </div>
</template>
