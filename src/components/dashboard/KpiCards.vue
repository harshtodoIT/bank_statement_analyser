<template>
  <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">

    <!-- Total Income -->
    <div class="relative bg-white rounded-2xl p-6 shadow-sm">
      <!-- Right indicator -->
      <div class="absolute right-3 top-6 h-12 w-1 rounded bg-green-500"></div>

      <!-- Icon -->
      <div class="w-10 h-10 rounded-lg bg-green-100 flex items-center justify-center mb-4">
        <svg
        class="w-5 h-5 text-green-600"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="2.5"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
    <path d="M4 14l6-6 4 4 6-6" />
    <path d="M16 6h4v4" />
        </svg>


      </div>

      <p class="text-sm text-gray-500">Total Income</p>
      <p class="text-3xl font-semibold text-green-600 mt-1">
        ₹74,249.50
      </p>
    </div>

    <!-- Total Expenses -->
    <div class="relative bg-white rounded-2xl p-6 shadow-sm">
      <!-- Right indicator -->
      <div class="absolute right-3 top-6 h-12 w-1 rounded bg-red-500"></div>

      <!-- Icon -->
      <div class="w-10 h-10 rounded-lg bg-red-100 flex items-center justify-center mb-4">
        <svg
  class="w-5 h-5 text-red-600"
  viewBox="0 0 24 24"
  fill="none"
  stroke="currentColor"
  stroke-width="2.5"
  stroke-linecap="round"
  stroke-linejoin="round"
>
  <path d="M4 10l6 6 4-4 6 6" />
  <path d="M16 18h4v-4" />
        </svg>


      </div>

      <p class="text-sm text-gray-500">Total Expenses</p>
      <p class="text-3xl font-semibold text-red-600 mt-1">
        ₹52,180.00
      </p>
    </div>

    <!-- Net Cash Flow -->
    <div class="relative bg-white rounded-2xl p-6 shadow-sm">
      <!-- Right indicator -->
      <div class="absolute right-3 top-6 h-12 w-1 rounded bg-blue-500"></div>

      <!-- Icon -->
      <div class="w-10 h-10 rounded-lg bg-blue-100 flex items-center justify-center mb-4">
        <span class="text-blue-600 text-lg font-semibold">₹</span>
      </div>

      <p class="text-sm text-gray-500">Net Cash Flow</p>
      <p class="text-3xl font-semibold text-blue-600 mt-1">
        ₹22,069.50
      </p>
    </div>

  </div>
</template>

<script setup>
</script>
