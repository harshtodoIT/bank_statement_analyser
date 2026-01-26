<script setup>
import KpiCards from "../components/dashboard/KpiCards.vue"
import HighLevelSummary from "../components/dashboard/HighLevelSummary.vue"
import IncomeExpenseChart from "../components/dashboard/IncomeExpenseChart.vue"
</script>

<template>
  <!-- Dashboard Page Wrapper -->
  <div class="min-h-full bg-transparent">
    <div>

      <!-- Header -->
      <!-- DASHBOARD HEADER -->
<div class="flex items-center justify-between mb-6">
  <!-- Left: Title -->
  <div>
    <h1 class="text-2xl font-semibold text-white">
      Dashboard
    </h1>
    <p class="text-slate-400">
      Financial Overview
    </p>
  </div>

  <!-- Right: Upload Button -->
  <button
    class="hidden sm:flex items-center gap-2
           px-4 py-2 rounded-lg text-sm font-medium
           bg-indigo-600 text-white
           hover:bg-indigo-700 transition"
    @click="$router.push('/upload')"
  >
    ⬆ Upload New Statement
  </button>
</div>


      <!-- Divider -->
      <div class="h-px bg-white/10 mb-8"></div>

      <!-- KPI Cards -->
      <section class="mb-8">
        <KpiCards />
      </section>

      <!-- Insights Section -->
      <section class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
        <IncomeExpenseChart />
        <HighLevelSummary />
      </section>

      <!-- Info / Privacy Banner -->
      <section
  class="rounded-2xl border border-white/10 bg-slate-800/60 backdrop-blur
         p-5 text-sm text-slate-300"
>
  <div class="flex items-start gap-3">
    <!-- Info icon -->
    <div
      class="flex h-9 w-9 items-center justify-center rounded-xl
             bg-indigo-500/20 text-indigo-400 shrink-0"
    >
      <!-- info icon -->
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-5 w-5"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M13 16h-1v-4h-1m1-4h.01M12 18a6 6 0 100-12 6 6 0 000 12z"
        />
      </svg>
    </div>

    <!-- Text -->
    <div>
      <p class="font-medium text-white">
        Privacy Notice
      </p>
      <p class="mt-1 text-slate-400 leading-relaxed">
        Your data is processed temporarily in memory and discarded.
        No information is stored unless you create an account.
      </p>
    </div>
  </div>
</section>


    </div>
  </div>
</template>
