<script setup>
import { ref, computed, onMounted } from "vue"
import { useRoute, useRouter } from "vue-router"
import { useProcessingStore } from "../stores/processing.store"
import { getCategoryDrillDown } from "../api/category.api"

const route = useRoute()
const router = useRouter()
const processingStore = useProcessingStore()

const categoryTitle = decodeURIComponent(route.params.category)

const loading = ref(true)
const error = ref(null)
const transactions = ref([])
const searchQuery = ref("")

const goBack = () => {
  router.push({
    path: "/dashboard/category-breakdown",
    query: { tab: "details" }
  })
}

/**
 * 🔹 FETCH CATEGORY TRANSACTIONS
 */
onMounted(async () => {
  try {
    if (!processingStore.jobId) {
      router.push("/upload")
      return
    }

    const res = await getCategoryDrillDown({
      job_id: processingStore.jobId,
      category: categoryTitle
    })

    transactions.value = res.transactions.map(tx => ({
      description: tx.description,
      date: tx.date,
      bank: tx.bank_name,
      amount: tx.debit ?? tx.credit ?? 0
    }))
  } catch {
    error.value = "Failed to load category data"
  } finally {
    loading.value = false
  }
})

/**
 * 🔹 SEARCH
 */
const filteredTransactions = computed(() => {
  const q = searchQuery.value.toLowerCase()
  return transactions.value.filter(tx =>
    tx.description.toLowerCase().includes(q) ||
    tx.bank.toLowerCase().includes(q)
  )
})

const highlightText = (text) => {
  if (!searchQuery.value) return text
  const q = searchQuery.value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")
  return text.replace(
    new RegExp(`(${q})`, "gi"),
    `<span class="bg-purple-100 text-purple-700 px-1 rounded">$1</span>`
  )
}

/**
 * 🔹 METRICS
 */
const totalAmount = computed(() =>
  transactions.value.reduce((s, t) => s + t.amount, 0)
)

const highestSpend = computed(() =>
  transactions.value.length
    ? Math.max(...transactions.value.map(t => t.amount))
    : 0
)

const averageSpend = computed(() =>
  transactions.value.length
    ? Math.round(totalAmount.value / transactions.value.length)
    : 0
)

</script>

<template>
  <div class="p-4 sm:p-6 space-y-6 sm:space-y-8">

    <!-- HEADER -->
    <div class="flex items-start sm:items-center gap-4">
      <button @click="goBack">←</button>
      <div>
        <h1 class="text-2xl font-semibold text-white">
          {{ categoryTitle }}
        </h1>
        <p class="text-sm text-slate-400">
          Spending insights & transactions
        </p>
      </div>
    </div>

    <!-- LOADING -->
    <div v-if="loading" class="text-slate-400">
      Loading transactions...
    </div>

    <!-- ERROR -->
    <div v-else-if="error" class="text-red-400">
      {{ error }}
    </div>

    <!-- CONTENT -->
    <template v-else>

      <!-- TOTAL -->
      <div class="rounded-2xl bg-slate-800 border border-white/10 p-6">
        <p class="text-sm text-slate-400">Total Spent</p>
        <h2 class="text-4xl font-bold text-purple-400 mt-2">
          ₹{{ totalAmount }}
        </h2>
      </div>

      <!-- INSIGHTS -->
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-6">
        <InsightCard label="Transactions" :value="transactions.length" />
        <InsightCard label="Highest Spend" :value="`₹${highestSpend}`" />
        <InsightCard label="Average Spend" :value="`₹${averageSpend}`" />
      </div>

      <!-- TRANSACTIONS -->
      <div class="rounded-2xl bg-slate-800 border border-white/10">
        <div class="px-6 py-4 border-b flex justify-between gap-4">
          <h3 class="text-lg font-semibold text-white">Transactions</h3>
          <input
            v-model="searchQuery"
            placeholder="Search by merchant or bank"
            class="rounded-full bg-slate-700 px-4 py-2 text-sm text-white"
          />
        </div>

        <div
          v-for="tx in filteredTransactions"
          :key="tx.description + tx.date"
          class="flex justify-between px-6 py-4 border-t border-white/5"
        >
          <div>
            <p
              class="font-medium text-white"
              v-html="highlightText(tx.description)"
            />
            <p class="text-sm text-slate-400">{{ tx.date }}</p>
          </div>

          <div class="text-right">
            <p class="text-sm text-slate-400">{{ tx.bank }}</p>
            <p class="font-semibold text-white">₹{{ tx.amount }}</p>
          </div>
        </div>
      </div>

    </template>
  </div>
</template>

<script>
export default {
  components: {
    InsightCard: {
      props: ["label", "value"],
      template: `
        <div class="rounded-xl bg-slate-800 border border-white/10 p-6">
          <p class="text-sm text-slate-400">{{ label }}</p>
          <p class="mt-2 text-2xl font-semibold text-white">{{ value }}</p>
        </div>
      `
    }
  }
}
</script>
