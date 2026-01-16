<template>
  <div class="bg-white rounded-2xl p-6 shadow-sm h-full">

    <h2 class="text-lg font-semibold text-gray-900 mb-6">
      High-Level Summary
    </h2>

    <div class="space-y-6">

      <!-- Total Transactions -->
      <div class="flex items-start gap-4">
        <div class="w-10 h-10 rounded-xl bg-blue-100 flex items-center justify-center">
          <span class="text-blue-600 font-semibold">₹</span>
        </div>
        <div>
          <p class="text-sm text-gray-500">Total Transactions Processed</p>
          <p class="text-lg font-semibold text-gray-900">347</p>
        </div>
      </div>

      <!-- Date Range -->
      <div class="flex items-start gap-4">
        <div class="w-10 h-10 rounded-xl bg-blue-100 flex items-center justify-center">
          📅
        </div>
        <div>
          <p class="text-sm text-gray-500">Statement Date Range</p>
          <p class="text-lg font-semibold text-gray-900">
            Jan 2024 – Jun 2024
          </p>
        </div>
      </div>

      <!-- Bank -->
      <div class="flex items-start gap-4">
        <div class="w-10 h-10 rounded-xl bg-blue-100 flex items-center justify-center">
          🏦
        </div>
        <div>
          <p class="text-sm text-gray-500">Bank Detected</p>
          <p class="text-lg font-semibold text-gray-900">Chase Bank</p>
        </div>
      </div>

      <!-- Account Type -->
      <div class="flex items-start gap-4">
        <div class="w-10 h-10 rounded-xl bg-blue-100 flex items-center justify-center">
          💳
        </div>
        <div>
          <p class="text-sm text-gray-500">Account Type</p>
          <p class="text-lg font-semibold text-gray-900">
            Checking Account
          </p>
        </div>
      </div>

    </div>
  </div>
</template>


<script setup>
</script>
