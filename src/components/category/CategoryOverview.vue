<script setup>
  import CategoryDonut from './CategoryDonut.vue'
  </script>

<template>
  <div class="flex flex-col items-center space-y-10">

    <!-- ================= Chart Card ================= -->
    <div
      class="w-full max-w-3xl bg-slate-800 rounded-2xl
             border border-white/10 p-6"
    >
      <h3 class="text-lg font-semibold text-white mb-6">
        Category Distribution
      </h3>

      <!-- Pie Chart -->
      <div class="flex justify-center">
        <CategoryDonut />
      </div>

      <!-- Legend -->
      <div class="flex justify-center gap-8 text-sm text-slate-300 mt-6">
        <div class="flex items-center gap-2">
          <span class="w-3 h-3 rounded-full bg-indigo-500"></span>
          <span>Income</span>
        </div>
        <div class="flex items-center gap-2">
          <span class="w-3 h-3 rounded-full bg-sky-500"></span>
          <span>Expenses</span>
        </div>
        <div class="flex items-center gap-2">
          <span class="w-3 h-3 rounded-full bg-slate-500"></span>
          <span>Uncategorized</span>
        </div>
      </div>
    </div>

    <!-- ================= Summary Cards ================= -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 w-full">

      <!-- Total Income -->
      <div
        class="bg-slate-800 border border-white/10
               rounded-2xl p-5"
      >
        <p class="text-sm font-medium text-slate-400">
          Total Income
        </p>
        <p class="mt-2 text-2xl font-semibold text-indigo-400">
          ₹6,650.00
        </p>
      </div>

      <!-- Total Expenses -->
      <div
        class="bg-slate-800 border border-white/10
               rounded-2xl p-5"
      >
        <p class="text-sm font-medium text-slate-400">
          Total Expenses
        </p>
        <p class="mt-2 text-2xl font-semibold text-sky-400">
          ₹4,150.00
        </p>
      </div>

      <!-- Net Balance -->
      <div
        class="bg-slate-800 border border-white/10
               rounded-2xl p-5"
      >
        <p class="text-sm font-medium text-slate-400">
          Net Balance
        </p>
        <p class="mt-2 text-2xl font-semibold text-violet-400">
          ₹2,500.00
        </p>
      </div>

    </div>

  </div>
</template>

