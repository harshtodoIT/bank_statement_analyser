<script setup>
import { ref, onMounted, computed } from "vue"
import { useRouter } from "vue-router"

import { useProcessingStore } from "../stores/processing.store"
import { useDashboardStore } from "../stores/dashboard.store"
import { usePrivacyStore } from "../stores/privacy.store"
import { getProcessingHistory } from "../api/history.api"

const router = useRouter()

const processingStore = useProcessingStore()
const dashboardStore = useDashboardStore()
const privacyStore = usePrivacyStore()

const runs = ref([])
const loading = ref(false)
const error = ref(null)

const isTemporary = computed(() => privacyStore.isTemporary)

onMounted(async () => {
  if (!privacyStore.loaded) return

  if (isTemporary.value) {
    runs.value = []
    return
  }

  loading.value = true
  error.value = null

  try {
    const res = await getProcessingHistory()
    runs.value = res.data ?? []
  } catch {
    error.value = "Failed to load history"
  } finally {
    loading.value = false
  }
})

const goToRun = (jobId) => {
  processingStore.setJob(jobId)
  dashboardStore.reset()
  router.push("/dashboard")
}
</script>

<template>
  <div class="px-6 py-6 space-y-6">

    <!-- Header -->
    <div>
      <h1 class="text-2xl font-semibold text-white">
        Processing History
      </h1>
      <p class="text-slate-400 text-sm mt-1">
        Previously analyzed bank statements
      </p>
    </div>

    <!-- TEMPORARY MODE NOTICE -->
    <div
      v-if="isTemporary"
      class="bg-slate-800 border border-white/10 rounded-xl p-6
             text-center text-slate-400"
    >
      <p class="text-lg font-medium text-white mb-2">
        History unavailable
      </p>
      <p class="text-sm">
        You selected temporary processing.
        Enable persist mode to access history.
      </p>
    </div>

    <!-- Loading -->
    <div
      v-else-if="loading"
      class="text-slate-400 text-sm text-center py-16"
    >
      Loading history…
    </div>

    <!-- Error -->
    <div
      v-else-if="error"
      class="text-red-400 text-sm text-center py-16"
    >
      {{ error }}
    </div>

    <!-- Empty -->
    <div
      v-else-if="!runs.length"
      class="text-slate-400 text-sm text-center py-16"
    >
      No previous statements found.
    </div>

    <!-- History cards -->
    <div v-else class="space-y-4">
      <div
        v-for="run in runs"
        :key="run.job_id"
        @click="goToRun(run.job_id)"
        class="bg-slate-800 border border-white/10 rounded-xl p-5
               cursor-pointer hover:bg-slate-700/70 transition"
      >
        <div class="flex justify-between items-center">
          <div>
            <p class="text-white font-semibold">
              {{ run.bank_name }} Bank
            </p>
            <p class="text-xs text-slate-400">
              {{ new Date(run.created_at).toLocaleString() }}
            </p>
          </div>

          <span
            class="text-sm font-semibold"
            :class="run.net_cash_flow >= 0 ? 'text-green-400' : 'text-sky-400'"
          >
            ₹{{ Math.abs(run.net_cash_flow).toLocaleString() }}
          </span>
        </div>

        <div class="mt-3 text-xs text-slate-400">
          Transactions: {{ run.total_transactions }}
        </div>
      </div>
    </div>

  </div>
</template>
