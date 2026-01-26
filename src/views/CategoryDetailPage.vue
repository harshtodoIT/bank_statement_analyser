<template>
<div class="p-4 sm:p-6 space-y-6 sm:space-y-8">

    <!-- Header -->
    <div
  class="flex items-start sm:items-center gap-4"
>


      <button
        @click="goBack">

        ←
      </button>

      <div>
        <h1 class="text-2xl font-semibold text-white">
          {{ categoryTitle }}
        </h1>
        <p class="text-sm text-slate-400">
          Spending insights & transactions
        </p>
      </div>
    </div>

    <!-- Total Spent Card -->
    <div class="rounded-2xl bg-slate-800 border border-white/10 p-6">
      <p class="text-sm text-slate-400">Total Spent</p>

      <div class="flex items-center gap-4 mt-2">
        <h2 class="text-4xl font-bold text-purple-400">
          ₹{{ totalAmount }}
        </h2>

        <span class="rounded-full bg-purple-500/20 px-3 py-1 text-xs text-purple-400">
          {{ percentage }}% of monthly spend
        </span>
      </div>

      <div class="mt-4 h-2 w-full rounded-full bg-white/10 overflow-hidden">
        <div
          class="h-full bg-purple-400 rounded-full"
          :style="{ width: percentage + '%' }"
        />
      </div>
    </div>

    <!-- Insight Cards -->
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-6">
      <InsightCard label="Transactions" :value="transactions.length" />
      <InsightCard label="Highest Spend" :value="`₹${highestSpend}`" />
      <InsightCard label="Average Spend" :value="`₹${averageSpend}`" />
    </div>

    <!-- Transactions -->
    <div class="rounded-2xl bg-slate-800 border border-white/10">
      <div class="px-6 py-4 border-b
         flex flex-col gap-3
         sm:flex-row sm:items-center sm:justify-between"
>
  <!-- Title -->
  <h3 class="text-lg font-semibold text-white">
    Transactions
  </h3>

  <!-- Search -->
  <input
    v-model="searchQuery"
    type="text"
    placeholder="Search by merchant or bank"
    class="
      w-full sm:w-72
      rounded-full
      border border-white/10
      bg-slate-700
      px-5 py-2.5 text-sm
      text-white placeholder-slate-400
      focus:outline-none
      focus:ring-2 focus:ring-purple-500/40
    "

  />
</div>


      <TransitionGroup
      name="fade"
      tag="div"
      class="divide-y divide-white/5"
    >

        <!-- 🟣 EMPTY STATE -->
        <div
          v-if="filteredTransactions.length === 0"
          class="flex flex-col items-center justify-center py-16 text-center"
        >
          <div
            class="h-14 w-14 rounded-full bg-purple-100
                  flex items-center justify-center mb-4 text-2xl"
          >
            🔍
          </div>

          <p class="text-lg font-semibold text-gray-900">
            No transactions found
          </p>

          <p class="text-sm text-gray-500 mt-1">
            Try searching with a different merchant or bank
          </p>
        </div>

<!-- 🟢 TRANSACTIONS LIST -->
        <div
          v-else
          v-for="tx in filteredTransactions"
          :key="tx.description + tx.date"
          class="flex flex-col sm:flex-row sm:items-center sm:justify-between
          gap-3 sm:gap-0 px-4 sm:px-6 py-4"

        >

        <div>
          <p
              class="font-medium text-white"
              v-html="highlightText(tx.description)"
            ></p>
          <p class="text-sm text-slate-400">{{ tx.date }}</p>
        </div>

        <div class="flex items-center justify-between sm:justify-start gap-4 sm:gap-6 w-full sm:w-auto">
          <!-- Bank -->
          <div class="h-8 w-8 rounded-full bg-blue-500/20 text-blue-400">
            <div
              class="h-8 w-8 rounded-full bg-blue-100
                    flex items-center justify-center text-xs font-semibold"
            >
              {{ tx.bank[0] }}
            </div>
            <span
            class="text-sm font-medium text-slate-500"
            v-html="highlightText(tx.bank)"
          ></span>


          </div>

          <!-- Amount -->
          <p class="font-semibold text-white">
            ₹{{ tx.amount }}
          </p>
        </div>
      </div>

    </TransitionGroup>

    </div>

  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

const goBack = () => {
  router.push({
    path: '/dashboard/category-breakdown',
    query: { tab: 'details' }
  })
}

const categoryMap = {
  food: 'Food & Dining',
  travel: 'Travel',
  shopping: 'Shopping',
  utilities: 'Utilities',
  transport: 'Transportation',
  healthcare: 'Healthcare'
}

const categoryKey = route.params.category
const categoryTitle = categoryMap[categoryKey] || 'Category'

const transactions = [
  { description: 'Starbucks Coffee', date: '20 Jan 2026', bank: 'HDFC', amount: 450 },
  { description: 'Pizza Palace', date: '18 Jan 2026', bank: 'ICICI', amount: 850 },
  { description: 'The Breakfast Club', date: '15 Jan 2026', bank: 'SBI', amount: 320 },
  { description: 'Fresh Juice Bar', date: '14 Jan 2026', bank: 'HDFC', amount: 180 }
]

const searchQuery = ref('')

const filteredTransactions = computed(() => {
  const query = searchQuery.value.toLowerCase()

  return transactions.filter(tx =>
    tx.description.toLowerCase().includes(query) ||
    tx.bank.toLowerCase().includes(query)
  )
})

const highlightText = (text) => {
  if (!searchQuery.value) return text

  const query = searchQuery.value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
  const regex = new RegExp(`(${query})`, 'gi')

  return text.replace(
    regex,
    `<span class="bg-purple-100 text-purple-700 px-1 rounded">$1</span>`
  )
}



const totalAmount = transactions.reduce((s, t) => s + t.amount, 0)
const percentage = 36

const highestSpend = computed(() =>
  Math.max(...transactions.map(t => t.amount))
)

const averageSpend = computed(() =>
  Math.round(totalAmount / transactions.length)
)

const InsightCard = {
  props: ['label', 'value'],
  template: `
    <div class="rounded-xl bg-slate-800 border border-white/10 p-6">
      <p class="text-sm text-slate-400">{{ label }}</p>
      <p class="mt-2 text-2xl font-semibold text-white">{{ value }}</p>
    </div>
  `
}

</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: all 0.25s ease;
}

.fade-enter-from {
  opacity: 0;
  transform: translateY(6px);
}

.fade-leave-to {
  opacity: 0;
  transform: translateY(-6px);
}
</style>
