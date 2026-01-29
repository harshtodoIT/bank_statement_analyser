<script setup>
import { ref, computed } from "vue"

const label = ref("")
const amount = ref("")
const note = ref("")

const manualEntries = ref([])

const hasEntries = computed(() => manualEntries.value.length > 0)

const addManualEntry = () => {
  if (!label.value || !amount.value) return

  manualEntries.value.push({
    label: label.value,
    amount: amount.value,
    note: note.value,
    date: new Date().toLocaleString()
  })

  label.value = ""
  amount.value = ""
  note.value = ""
}

const manualTotal = computed(() => {
  return manualEntries.value.reduce((sum, entry) => {
    const value = Number(entry.amount)
    return isNaN(value) ? sum : sum + value
  }, 0)
})
</script>

<template>
  <div class="w-full px-6 py-6 max-w-4xl text-slate-200">

    <!-- HEADER -->
    <div class="mb-6">
      <h1 class="text-2xl font-semibold text-white">
        Manual Adjustments
      </h1>
      <p class="text-sm text-slate-400 mt-1">
        Add entries not present in your bank statement
      </p>
    </div>

    <!-- FORM CARD -->
    <div class="bg-slate-800 border border-white/10 rounded-xl p-6 space-y-5">

      <div>
        <label class="text-sm font-medium text-slate-300">
          Label <span class="text-indigo-400">*</span>
        </label>
        <input
          v-model="label"
          type="text"
          placeholder="e.g. Cash received from client"
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
          placeholder="e.g. +5000 or -1200"
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
          placeholder="Optional explanation or reference"
          class="w-full mt-1 px-4 py-2 rounded-lg
                 bg-slate-700 text-white placeholder-slate-400
                 focus:outline-none focus:ring-2 focus:ring-indigo-500/40"
        />
      </div>

      <button
        @click="addManualEntry"
        class="bg-indigo-600 hover:bg-indigo-700
               text-white px-5 py-2 rounded-lg transition"
      >
        Add Manual Entry
      </button>
    </div>

    <!-- SHOWN ONLY AFTER ADD -->
    <div v-if="hasEntries" class="mt-8 space-y-6">

      <!-- MANUAL ENTRIES -->
      <div class="bg-slate-800 border border-white/10 rounded-xl p-6">
        <h2 class="text-lg font-semibold mb-4 text-white">
          Manual Entries
        </h2>

        <div
          v-for="(entry, index) in manualEntries"
          :key="index"
          class="bg-slate-700/60 border border-white/5 rounded-lg
                 p-4 flex justify-between"
        >
          <div>
            <p class="font-medium text-white">
              {{ entry.label }}
              <span
                class="ml-2 text-xs bg-indigo-500/20
                       text-indigo-400 px-2 py-0.5 rounded"
              >
                Manual Entry
              </span>
            </p>

            <p class="text-sm text-slate-400 mt-1">
              {{ entry.note || "—" }}
            </p>

            <p class="text-xs text-slate-500 mt-1">
              {{ entry.date }}
            </p>
          </div>

          <div
            :class="[
              'font-semibold',
              entry.amount.startsWith('+')
                ? 'text-green-400'
                : 'text-sky-400'
            ]"
          >
            {{ entry.amount }}
          </div>
        </div>
      </div>

      <!-- TOTAL CARD -->
      <div
        class="bg-slate-800/60 border border-white/10
               rounded-xl p-5 flex justify-between"
      >
        <div>
          <p class="text-sm font-medium text-slate-300">
            Manual Entries Total
          </p>
          <p class="text-xs text-slate-400">
            Manual entries are included in totals
          </p>
        </div>

        <p
          class="text-lg font-semibold"
          :class="manualTotal >= 0 ? 'text-green-400' : 'text-red-400'"
        >
          {{ manualTotal >= 0 ? '+' : '-' }}₹{{ Math.abs(manualTotal).toLocaleString() }}
        </p>
      </div>

    </div>

  </div>
</template>
