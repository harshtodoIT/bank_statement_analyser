<script setup>
  import CategoryRow from './CategoryRow.vue'

  const categories = [
    {
      name: 'Food & Dining',
      amount: 2450,
      percent: 36,
      icon: 'food',
      color: 'purple'
    },
    {
      name: 'Travel',
      amount: 1820,
      percent: 27,
      icon: 'travel',
      color: 'blue'
    },
    {
      name: 'Shopping',
      amount: 1360,
      percent: 20,
      icon: 'shopping',
      color: 'purple'
    },
    {
      name: 'Utilities',
      amount: 680,
      percent: 10,
      icon: 'utilities',
      color: 'gray'
    },
    {
      name: 'Transportation',
      amount: 340,
      percent: 5,
      icon: 'transport',
      color: 'cyan'
    },
    {
      name: 'Healthcare',
      amount: 150,
      percent: 2,
      icon: 'healthcare',
      color: 'purple'
    }
  ]
  </script>

<template>
  <div class="space-y-6 text-slate-200">

    <!-- ================= HEADER ================= -->
    <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-2">
      <h2 class="text-lg font-semibold text-white">
        Category-wise Breakdown
      </h2>
      <p class="text-sm text-slate-400">
        Click on a category to view detailed transactions
      </p>
    </div>

    <!-- ================= CATEGORY GRID ================= -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <CategoryRow
        v-for="category in categories"
        :key="category.name"
        :name="category.name"
        :amount="category.amount"
        :percent="category.percent"
        :icon="category.icon"
        :color="category.color"
      />
    </div>

  </div>
</template>
