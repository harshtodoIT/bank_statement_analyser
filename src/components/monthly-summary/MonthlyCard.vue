<script setup>
defineProps({
  month: String,
  income: Number,
  expenses: Number,
  net_cash_flow: Number
})
</script>

<template>
  <div
    class="bg-white rounded-xl border p-4 sm:p-5 shadow-sm
           hover:shadow-md transition"
  >
    <h3 class="text-base sm:text-lg font-semibold mb-3">
      {{ month }}
    </h3>

    <div class="space-y-2 text-sm">
      <div class="flex justify-between">
        <span class="text-gray-500">Income</span>
        <span class="font-medium">₹{{ income }}</span>
      </div>

      <div class="flex justify-between">
        <span class="text-gray-500">Expenses</span>
        <span class="font-medium">₹{{ expenses }}</span>
      </div>

      <div class="flex justify-between pt-2 border-t">
        <span class="text-gray-500">Net Cash Flow</span>

        <span
          class="font-semibold flex items-center gap-1"
          :class="net_cash_flow >= 0 ? 'text-green-600' : 'text-red-600'"
        >
          <span>
            {{ net_cash_flow >= 0 ? ':arrow_upper_right:' : ':arrow_lower_right:' }}
          </span>
          ₹{{ Math.abs(net_cash_flow) }}
        </span>
      </div>
    </div>
  </div>
</template>
