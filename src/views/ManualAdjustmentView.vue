<script setup>
  import { ref } from 'vue'

  const label = ref('')
  const amount = ref('')
  const note = ref('')

  const hasEntries = ref(false)

  const manualEntries = ref([])

  const addManualEntry = () => {
    if (!label.value || !amount.value) return

    manualEntries.value.push({
      label: label.value,
      amount: amount.value,
      note: note.value,
      date: new Date().toLocaleString()
    })

    hasEntries.value = true

    // reset form
    label.value = ''
    amount.value = ''
    note.value = ''
  }
  </script>

  <template>
    <div class="w-full px-6 py-6 max-w-4xl">

      <!-- HEADER -->
      <div class="mb-6">
        <h1 class="text-2xl font-semibold text-gray-900">
          Manual Adjustments
        </h1>
        <p class="text-sm text-gray-500 mt-1">
          Add entries not present in your bank statement
        </p>
      </div>

      <!-- FORM CARD -->
      <div class="bg-white border rounded-xl p-6 space-y-5">

        <div>
          <label class="text-sm font-medium">
            Label <span class="text-red-500">*</span>
          </label>
          <input
            v-model="label"
            type="text"
            placeholder="e.g. Cash received from client"
            class="w-full mt-1 px-4 py-2 rounded-lg bg-gray-100 focus:outline-none"
          />
        </div>

        <div>
          <label class="text-sm font-medium">
            Amount <span class="text-red-500">*</span>
          </label>
          <input
            v-model="amount"
            type="text"
            placeholder="e.g. +5000 or -1200"
            class="w-full mt-1 px-4 py-2 rounded-lg bg-gray-100 focus:outline-none"
          />
          <p class="text-xs text-gray-500 mt-1">
            Use + for income, - for expense
          </p>
        </div>

        <div>
          <label class="text-sm font-medium">Note</label>
          <input
            v-model="note"
            type="text"
            placeholder="Optional explanation or reference"
            class="w-full mt-1 px-4 py-2 rounded-lg bg-gray-100 focus:outline-none"
          />
        </div>

        <button
          @click="addManualEntry"
          class="bg-slate-800 text-white px-5 py-2 rounded-lg hover:bg-slate-900"
        >
          Add Manual Entry
        </button>
      </div>

      <!-- =============================
           SHOWN ONLY AFTER ADD
      ============================== -->
      <div v-if="hasEntries" class="mt-8 space-y-6">

        <!-- MANUAL ENTRIES -->
        <div class="bg-white border rounded-xl p-6">
          <h2 class="text-lg font-semibold mb-4">
            Manual Entries
          </h2>

          <div
            v-for="(entry, index) in manualEntries"
            :key="index"
            class="bg-yellow-50 border border-yellow-200 rounded-lg p-4 flex justify-between"
          >
            <div>
              <p class="font-medium">
                {{ entry.label }}
                <span class="ml-2 text-xs bg-yellow-200 px-2 py-0.5 rounded">
                  Manual Entry
                </span>
              </p>

              <p class="text-sm text-gray-500 mt-1">
                {{ entry.note || '—' }}
              </p>

              <p class="text-xs text-gray-400 mt-1">
                {{ entry.date }}
              </p>
            </div>

            <div
              :class="[
                'font-semibold',
                entry.amount.startsWith('+') ? 'text-green-600' : 'text-red-600'
              ]"
            >
              {{ entry.amount }}
            </div>
          </div>
        </div>

        <!-- TOTAL CARD -->
        <div class="bg-blue-50 border border-blue-200 rounded-xl p-5 flex justify-between">
          <div>
            <p class="text-sm font-medium">
              Manual Entries Total
            </p>
            <p class="text-xs text-gray-500">
              Manual entries are included in totals
            </p>
          </div>

          <p class="text-lg font-semibold text-blue-700">
            +2,000.00
          </p>
        </div>

      </div>

    </div>
  </template>
