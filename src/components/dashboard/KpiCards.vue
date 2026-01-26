<template>
  <!-- KPI Cards -->
  <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-6">

    <!-- Total Income -->
    <div class="bg-slate-800 rounded-2xl shadow-sm border border-white/5 p-6 flex justify-between items-start">
      <div>
        <p class="text-sm text-slate-400">Total Income</p>
        <h2 class="text-3xl font-bold text-white">₹10,200</h2>
        <p class="text-sm text-green-600 mt-2">+4.2% from last month</p>
      </div>

      <div class="bg-green-500/20 text-green-400 rounded-xl p-3 h-fit">
        <!-- Up arrow icon -->
        <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none"
          viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="M5 10l7-7m0 0l7 7m-7-7v18" />
        </svg>
      </div>
    </div>

    <!-- Total Expenses -->
    <div class="bg-slate-800 rounded-2xl shadow-sm border border-white/5 p-6 flex justify-between items-start">
      <div>
        <p class="text-sm text-slate-400">Total Expenses</p>
        <h2 class="text-3xl font-bold text-white mt-2">₹6,800</h2>
        <p class="text-sm text-indigo-600 mt-2">+8.1% from last month</p>
      </div>

      <div class="bg-indigo-500/20 text-indigo-400 rounded-xl p-3 h-fit">
        <!-- Down arrow icon -->
        <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none"
          viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="M19 14l-7 7m0 0l-7-7m7 7V3" />
        </svg>
      </div>
    </div>

    <!-- Current Balance -->
    <div class="bg-slate-800 rounded-2xl shadow-sm border border-white/5 p-6 flex justify-between items-start">
      <div>
        <p class="text-sm text-slate-400">Current Balance</p>
        <h2 class="text-3xl font-bold text-white mt-2">₹3,400</h2>
        <p class="text-sm text-gray-500 mt-2">Available balance</p>
      </div>

      <div class="bg-slate-700 text-slate-300 rounded-xl p-3 h-fit">
        <!-- Wallet icon -->
        <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none"
          viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-2m4-3h-6a2 2 0 000 4h6v-4z" />
        </svg>
      </div>
    </div>

  </div>
</template>


<script setup>
</script>
