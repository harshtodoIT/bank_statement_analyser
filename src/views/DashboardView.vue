<script setup>
import { computed, onMounted } from "vue"
import { useRouter } from "vue-router"
import { useDashboardStore } from "../stores/dashboard.store"
import { useProcessingStore } from "../stores/processing.store"
import { useUploadStore } from "../stores/upload.store"

import KpiCards from "../components/dashboard/KpiCards.vue"
import HighLevelSummary from "../components/dashboard/HighLevelSummary.vue"
import IncomeExpenseChart from "../components/dashboard/IncomeExpenseChart.vue"

const router = useRouter()
const dashboardStore = useDashboardStore()
const processingStore = useProcessingStore()
const uploadStore = useUploadStore()

onMounted(async () => {
  if (!processingStore.jobId) {
    router.replace("/upload")
    return
  }

  await dashboardStore.fetchDashboardData(processingStore.jobId)
})

const isReady = computed(() => dashboardStore.loaded && !dashboardStore.loading)

const startNewUpload = () => {
  processingStore.reset()
  dashboardStore.reset()
  uploadStore.reset()
  router.push("/upload")
}
</script>

<template>
  <div class="min-h-full bg-transparent">

    <!-- LOADING STATE -->
    <div
      v-if="!isReady"
      class="flex items-center justify-center py-24 text-slate-400"
    >
      Loading dashboard…
    </div>

    <!-- DASHBOARD -->
    <div v-else>
      <div class="flex items-center justify-between mb-6">
        <div>
          <h1 class="text-2xl font-semibold text-white">Dashboard</h1>
          <p class="text-slate-400">Financial Overview</p>
        </div>

        <button
          class="hidden sm:flex items-center gap-2 px-4 py-2 rounded-lg
                 text-sm font-medium bg-indigo-600 text-white
                 hover:bg-indigo-700 transition"
          @click="startNewUpload"
        >
          ↑ Upload New Statement
        </button>
      </div>

      <div class="h-px bg-white/10 mb-8"></div>

      <section class="mb-8">
        <KpiCards />
      </section>

      <section class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
        <IncomeExpenseChart />
        <HighLevelSummary />
      </section>

      <section
        class="rounded-2xl border border-white/10 bg-slate-800/60
               backdrop-blur p-5 text-sm text-slate-300"
      >
        <p class="font-medium text-white">Privacy Notice</p>
        <p class="mt-1 text-slate-400">
          Your data is processed temporarily and discarded.
        </p>
      </section>
    </div>

  </div>
</template>
