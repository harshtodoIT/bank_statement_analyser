<script setup>
import { computed, ref, onMounted } from "vue"
import { useDashboardStore } from "../../stores/dashboard.store"

const dashboardStore = useDashboardStore()
const animated = ref(false)

const months = computed(() => {
  const summary = dashboardStore.monthlySummary ?? {}

  return Object.entries(summary).map(([month, values]) => ({
    name: month,
    income: Number(values?.income ?? 0),
    expense: Number(values?.expense ?? 0),
  }))
})

const maxValue = computed(() => {
  if (!months.value.length) return 1

  const all = months.value.flatMap(m => [m.income, m.expense])
  const max = Math.max(...all)

  return Number.isFinite(max) && max > 0 ? max : 1
})

const chartHeight = 220

onMounted(() => {
  setTimeout(() => {
    animated.value = true
  }, 100)
})
</script>

<template>
  <div class="bg-slate-800 rounded-2xl p-6 border border-white/5">

    <h2 class="text-lg font-semibold text-white mb-6">
      Income vs Expenses Overview
    </h2>

    <div v-if="!months.length" class="text-sm text-slate-400">
      No monthly data available
    </div>

    <div v-else class="overflow-x-auto lg:overflow-x-hidden scrollbar-hide">
      <div class="relative flex min-w-[640px]">

        <!-- Y Axis -->
        <div class="flex flex-col justify-between h-[220px] pr-4 text-sm text-slate-400 shrink-0">
          <span>₹{{ maxValue }}</span>
          <span>₹{{ Math.round(maxValue * 0.75) }}</span>
          <span>₹{{ Math.round(maxValue * 0.5) }}</span>
          <span>₹{{ Math.round(maxValue * 0.25) }}</span>
          <span>₹0</span>
        </div>

        <!-- Chart Area -->
        <div class="relative flex-1">

          <!-- Grid Lines -->
          <div class="absolute inset-0 flex flex-col justify-between">
            <div
              v-for="i in 5"
              :key="i"
              class="border-t border-dashed border-white/10"
            ></div>
          </div>

          <!-- Bars -->
          <div class="relative flex items-end h-[220px] gap-6 px-4">

            <div
              v-for="month in months"
              :key="month.name"
              class="flex flex-col items-center w-[72px]"
            >
              <div class="flex items-end gap-2 h-full">

                <!-- Income -->
                <div
                  class="w-6 rounded-md transition-all duration-700 ease-out
                         bg-gradient-to-t from-emerald-700 via-emerald-600 to-emerald-400
                         shadow-[0_0_14px_rgba(16,185,129,0.28)]"
                  :style="{
                    height: animated
                      ? (month.income / maxValue) * chartHeight + 'px'
                      : '0px'
                  }"
                ></div>

                <!-- Expense -->
                <div
                  class="w-6 rounded-md transition-all duration-700 ease-out
                         bg-gradient-to-t from-sky-700 via-sky-600 to-sky-400
                         shadow-[0_0_14px_rgba(14,165,233,0.28)]"
                  :style="{
                    height: animated
                      ? (month.expense / maxValue) * chartHeight + 'px'
                      : '0px'
                  }"
                ></div>

              </div>

              <!-- Month -->
              <span class="mt-3 text-sm text-slate-400">
                {{ month.name }}
              </span>
            </div>

          </div>

          <!-- X Axis -->
          <div class="absolute bottom-[28px] left-0 right-0 border-t border-white/20"></div>

        </div>
      </div>
    </div>

    <!-- Legend -->
    <div class="flex justify-center gap-6 mt-6 text-sm text-slate-300">
      <div class="flex items-center gap-2">
        <span class="w-3 h-3 rounded-full bg-emerald-500"></span>
        Income
      </div>
      <div class="flex items-center gap-2">
        <span class="w-3 h-3 rounded-full bg-sky-500"></span>
        Expenses
      </div>
    </div>

  </div>
</template>
