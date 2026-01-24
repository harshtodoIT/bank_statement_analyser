<template>
<div class="p-4 sm:p-6 space-y-6 sm:space-y-8">

    <!-- Header -->
<div
  class="sticky top-0 z-30
         bg-white
         border-b border-gray-200
         shadow-sm
         flex items-start sm:items-center gap-4
         -mx-4 px-4 py-3
         sm:static sm:mx-0 sm:px-0 sm:py-0
         sm:border-b-0 sm:shadow-none"
>

      <button
        @click="goBack">

        ←
      </button>

      <div>
        <h1 class="text-2xl font-semibold text-gray-900">
          {{ categoryTitle }}
        </h1>
        <p class="text-sm text-gray-500">
          Spending insights & transactions
        </p>
      </div>
    </div>

    <!-- Total Spent Card -->
    <div class="rounded-2xl bg-white p-6 shadow-sm">
      <p class="text-sm text-gray-500">Total Spent</p>

      <div class="flex items-center gap-4 mt-2">
        <h2 class="text-4xl font-bold text-purple-600">
          ₹{{ totalAmount }}
        </h2>

        <span class="rounded-full bg-purple-100 px-3 py-1 text-xs text-purple-600">
          {{ percentage }}% of monthly spend
        </span>
      </div>

      <div class="mt-4 h-2 w-full rounded-full bg-gray-100 overflow-hidden">
        <div
          class="h-full bg-purple-500 rounded-full"
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
    <div class="rounded-2xl bg-white shadow-sm">
      <div class="px-6 py-4 border-b
         flex flex-col gap-3
         sm:flex-row sm:items-center sm:justify-between"
>
  <!-- Title -->
  <h3 class="text-lg font-semibold text-gray-900">
    Transactions
  </h3>

  <!-- Search -->
  <input
    v-model="searchQuery"
    type="text"
    placeholder="Search by merchant or bank"
    class="
      w-full
      sm:w-72
      rounded-full border border-gray-200 bg-white
      px-5 py-2.5 text-sm shadow-sm
      focus:outline-none focus:ring-2 focus:ring-purple-400
    "
  />
</div>


      <TransitionGroup
      name="fade"
      tag="div"
      class="divide-y"
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
              class="font-medium text-gray-900"
              v-html="highlightText(tx.description)"
            ></p>
          <p class="text-sm text-gray-500">{{ tx.date }}</p>
        </div>

        <div class="flex items-center justify-between sm:justify-start gap-4 sm:gap-6 w-full sm:w-auto">
          <!-- Bank -->
          <div class="flex items-center gap-2">
            <div
              class="h-8 w-8 rounded-full bg-blue-100
                    flex items-center justify-center text-xs font-semibold"
            >
              {{ tx.bank[0] }}
            </div>
            <span
                class="text-sm text-gray-700"
                v-html="highlightText(tx.bank)"
              ></span>
          </div>

          <!-- Amount -->
          <p class="font-semibold text-gray-900">
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
    <div class="rounded-xl bg-white p-6 shadow-sm">
      <p class="text-sm text-gray-500">{{ label }}</p>
      <p class="mt-2 text-2xl font-semibold text-gray-900">{{ value }}</p>
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
