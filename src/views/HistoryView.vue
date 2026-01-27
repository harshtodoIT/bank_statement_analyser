<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

/**
 * Simulated backend response (same shape you shared)
 */
const allRuns = [
  {
    run_id: 'run_001',
    bank_name: 'HDFC',
    start_date: '2024-01-01',
    end_date: '2024-05-31',
    uploaded_at: '2026-01-20T12:10:00Z',
    total_transactions: 36,
    net_cash_flow: 28850
  },
  {
    run_id: 'run_002',
    bank_name: 'ICICI',
    start_date: '2023-10-01',
    end_date: '2023-12-31',
    uploaded_at: '2025-12-15T09:40:00Z',
    total_transactions: 22,
    net_cash_flow: -11300
  },
  {
    run_id: 'run_003',
    bank_name: 'SBI',
    start_date: '2024-06-01',
    end_date: '2024-09-30',
    uploaded_at: '2026-01-10T18:30:00Z',
    total_transactions: 41,
    net_cash_flow: 40500
  }
]

/**
 * Infinite scroll simulation
 */
const visibleRuns = ref([])
const page = ref(1)
const pageSize = 2
const loading = ref(false)
const hasMore = ref(true)

const loadMore = () => {
  if (loading.value || !hasMore.value) return

  loading.value = true

  setTimeout(() => {
    const start = (page.value - 1) * pageSize
    const next = allRuns.slice(start, start + pageSize)

    if (!next.length) {
      hasMore.value = false
    } else {
      visibleRuns.value.push(...next)
      page.value++
    }

    loading.value = false
  }, 600)
}

onMounted(() => {
  loadMore()
})

const goToRun = (runId) => {
  router.push(`/dashboard?run_id=${runId}`)
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

    <!-- EMPTY STATE -->
    <div
      v-if="!visibleRuns.length && !loading"
      class="text-slate-400 text-sm text-center py-16"
    >
      No previous statements found.
    </div>

    <!-- HISTORY CARDS -->
    <div class="space-y-4">
      <div
        v-for="run in visibleRuns"
        :key="run.run_id"
        @click="goToRun(run.run_id)"
        class="bg-slate-800 border border-white/10 rounded-xl p-5
               cursor-pointer hover:bg-slate-700/70 transition"
      >
        <!-- Top row -->
        <div class="flex justify-between items-center">
          <div>
            <p class="text-white font-semibold">
              {{ run.bank_name }} Bank
            </p>
            <p class="text-xs text-slate-400">
              {{ run.start_date }} → {{ run.end_date }}
            </p>
          </div>

          <span
            class="text-sm font-semibold"
            :class="run.net_cash_flow >= 0 ? 'text-green-400' : 'text-sky-400'"
          >
            ₹{{ Math.abs(run.net_cash_flow).toLocaleString() }}
          </span>
        </div>

        <!-- Meta -->
        <div class="mt-3 flex flex-wrap gap-6 text-xs text-slate-400">
          <span>
            Uploaded:
            {{ new Date(run.uploaded_at).toLocaleString() }}
          </span>
          <span>
            Transactions: {{ run.total_transactions }}
          </span>
        </div>
      </div>
    </div>

    <!-- LOADER -->
    <div v-if="loading" class="text-center text-slate-400 text-sm py-4">
      Loading more history…
    </div>

    <!-- LOAD MORE (infinite scroll fallback) -->
    <div v-if="hasMore && !loading" class="text-center">
      <button
        @click="loadMore"
        class="text-sm text-indigo-400 hover:underline"
      >
        Load more
      </button>
    </div>

  </div>
</template>
