<script setup>
import { ref, computed } from "vue"
import { useProcessingStore } from "../stores/processing.store"
import { useDashboardStore } from "../stores/dashboard.store"
import api from "../api/apiClient"

const processingStore = useProcessingStore()
const dashboardStore = useDashboardStore()

const label = ref("")
const amount = ref("")
const note = ref("")

const loading = ref(false)
const error = ref(null)
const success = ref(false)

/**
 * Manual entries from backend (SOURCE OF TRUTH)
 */
const manualAdjustments = computed(
  () => dashboardStore.manualAdjustments || []
)

/**
 * Validate amount format
 */
const isValidAmount = computed(() => {
  return /^[-+]?\d+(\.\d+)?$/.test(amount.value)
})

/**
 * Submit manual adjustment
 */
const addManualEntry = async () => {
  error.value = null
  success.value = false

  if (!processingStore.jobId) {
    error.value = "No active job found"
    return
  }

  if (!label.value || !amount.value || !isValidAmount.value) {
    error.value = "Please provide a valid label and amount"
    return
  }

  loading.value = true

  try {
    await api.post(
      `/adjustments/${processingStore.jobId}/`,
      {
        label: label.value.trim(),
        amount: Number(amount.value),
        note: note.value?.trim() || ""
      }
    )

    /**
     * 🔄 Refetch dashboard so:
     * - Net cash flow updates
     * - Manual list updates
     */
    dashboardStore.reset()
    await dashboardStore.fetchDashboardData(processingStore.jobId)

    label.value = ""
    amount.value = ""
    note.value = ""
    success.value = true
  } catch {
    error.value = "Failed to add manual adjustment"
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="w-full px-6 py-6 max-w-4xl text-slate-200 space-y-8">

    <!-- HEADER -->
    <div>
      <h1 class="text-2xl font-semibold text-white">
        Manual Adjustments
      </h1>
      <p class="text-sm text-slate-400 mt-1">
        Add entries not present in your bank statement
      </p>
    </div>

    <!-- FORM -->
    <div class="bg-slate-800 border border-white/10 rounded-xl p-6 space-y-5">

      <div v-if="error" class="text-red-400 text-sm">
        {{ error }}
      </div>

      <div v-if="success" class="text-green-400 text-sm">
        Manual adjustment added successfully
      </div>

      <div>
        <label class="text-sm font-medium text-slate-300">
          Label <span class="text-indigo-400">*</span>
        </label>
        <input
          v-model="label"
          type="text"
          placeholder="e.g. Cash given to vendor"
          class="w-full mt-1 px-4 py-2 rounded-lg
                 bg-slate-700 text-white placeholder-slate-400
                 focus:outline-none focus:ring-2 focus:ring-indigo-500/40"
        />
      </div>

      <div>
        <label class="text-sm font-medium text-slate-300">
          Amount <span class="text-indigo-400">*</span>
        </label>
        <input
          v-model="amount"
          type="text"
          placeholder="+5000 or -1200"
          class="w-full mt-1 px-4 py-2 rounded-lg
                 bg-slate-700 text-white placeholder-slate-400
                 focus:outline-none focus:ring-2 focus:ring-indigo-500/40"
        />
        <p class="text-xs text-slate-400 mt-1">
          Use + for income, - for expense
        </p>
      </div>

      <div>
        <label class="text-sm font-medium text-slate-300">
          Note
        </label>
        <input
          v-model="note"
          type="text"
          placeholder="Optional explanation"
          class="w-full mt-1 px-4 py-2 rounded-lg
                 bg-slate-700 text-white placeholder-slate-400
                 focus:outline-none focus:ring-2 focus:ring-indigo-500/40"
        />
      </div>

      <button
        @click="addManualEntry"
        :disabled="loading"
        class="bg-indigo-600 hover:bg-indigo-700
               disabled:opacity-60
               text-white px-5 py-2 rounded-lg transition"
      >
        {{ loading ? "Saving..." : "Add Manual Entry" }}
      </button>
    </div>

    <!-- MANUAL ENTRIES LIST -->
    <div
      v-if="manualAdjustments.length"
      class="bg-slate-800 border border-white/10 rounded-xl p-6 space-y-4"
    >
      <h2 class="text-lg font-semibold text-white">
        Manual Entries
      </h2>

      <div
        v-for="(entry, index) in manualAdjustments"
        :key="index"
        class="bg-slate-700/60 border border-white/5 rounded-lg
               p-4 flex justify-between items-start"
      >
        <div>
          <p class="font-medium text-white">
            {{ entry.label }}
            <span
              class="ml-2 text-xs bg-indigo-500/20
                     text-indigo-400 px-2 py-0.5 rounded"
            >
              Manual
            </span>
          </p>

          <p class="text-sm text-slate-400 mt-1">
            {{ entry.note || "No note" }}
          </p>
        </div>

        <div
          class="font-semibold"
          :class="entry.amount >= 0 ? 'text-green-400' : 'text-red-400'"
        >
          {{ entry.amount >= 0 ? '+' : '-' }}₹{{ Math.abs(entry.amount).toLocaleString() }}
        </div>
      </div>
    </div>

    <!-- EMPTY STATE -->
    <div
      v-else
      class="text-slate-400 text-sm text-center"
    >
      No manual adjustments added yet.
    </div>

  </div>
</template>
