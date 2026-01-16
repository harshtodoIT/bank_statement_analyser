<template>
  <div class="border border-dashed border-orange-400 bg-orange-50 rounded-xl p-4">
    <div class="flex items-start gap-3">
      <div class="h-8 w-8 flex items-center justify-center rounded-full bg-orange-100 text-orange-600">
        !
      </div>

      <div class="flex-1">
        <h4 class="font-semibold text-orange-700">
          Uncategorized Transactions
        </h4>
        <p class="text-sm text-orange-600">
          {{ count }} transactions need categorization
        </p>

        <div class="mt-3 h-2 bg-orange-200 rounded-full overflow-hidden">
          <div
            class="h-full bg-orange-400 rounded-full"
            :style="{ width: percentage + '%' }"
          />
        </div>
      </div>

      <div class="text-right font-semibold text-orange-700">
        ₹{{ amount.toLocaleString() }}
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  count: Number,
  amount: Number,
  percentage: Number
})
</script>

