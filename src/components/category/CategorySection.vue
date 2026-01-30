<script setup>
import CategoryRow from "./CategoryRow.vue"

defineProps({
  title: String,
  total: Number,
  type: String,
  categories: {
    type: Array,
    default: () => []
  }
})
</script>

<template>
  <div class="space-y-4">

    <!-- Section Header -->
    <div
      class="flex justify-between items-center rounded-lg px-4 py-3"
      :class="{
        'bg-green-50 text-green-700': type === 'income',
        'bg-red-50 text-red-700': type === 'expense',
        'bg-orange-50 text-orange-700': type === 'uncategorized'
      }"
    >
      <p class="font-medium">
        {{ title }}
      </p>
      <p class="font-semibold">
        ₹{{ total.toLocaleString() }}
      </p>
    </div>

    <!-- Rows -->
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
</template>
