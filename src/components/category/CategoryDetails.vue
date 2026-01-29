<script setup>
import { computed } from "vue"
import { useDashboardStore } from "../../stores/dashboard.store"
import CategoryRow from "./CategoryRow.vue"

const store = useDashboardStore()

/**
 * EXPENSE CATEGORIES
 * already prepared correctly in dashboard.store.js
 */
const expenseCategories = computed(() => {
  return store.expenseCategories || []
})

/**
 * UNCATEGORIZED
 */
const uncategorizedCategories = computed(() => {
  return store.uncategorizedAmount
    ? [{
        name: "Uncategorized",
        amount: store.uncategorizedAmount,
        percent: 100,
        icon: "uncategorized",
        color: "gray"
      }]
    : []
})
</script>

<template>
  <div class="space-y-8 text-slate-200">

    <!-- HEADER -->
    <div class="flex justify-between items-center">
      <h2 class="text-lg font-semibold text-white">
        Category-wise Breakdown
      </h2>
      <p class="text-sm text-slate-400">
        Click on a category to view detailed transactions
      </p>
    </div>

    <!-- EXPENSE CATEGORIES -->
    <div v-if="expenseCategories.length">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <CategoryRow
          v-for="category in expenseCategories"
          :key="category.name"
          :name="category.name"
          :amount="category.amount"
          :percent="category.percent"
          icon="expense"
          color="indigo"
        />
      </div>
    </div>

    <!-- UNCATEGORIZED -->
    <div v-if="uncategorizedCategories.length">
      <h3 class="text-sm font-semibold text-slate-300 mt-10 mb-3">
        Uncategorized
      </h3>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <CategoryRow
          v-for="category in uncategorizedCategories"
          :key="category.name"
          :name="category.name"
          :amount="category.amount"
          :percent="category.percent"
          :icon="category.icon"
          :color="category.color"
        />
      </div>
    </div>

  </div>
</template>
