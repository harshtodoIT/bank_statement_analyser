<script setup>
  import CategoryDonut from './CategoryDonut.vue'
  </script>

  <template>
    <div class="flex flex-col items-center space-y-10">

      <!-- Chart Card -->
      <div class="w-full max-w-3xl bg-white rounded-2xl border border-gray-100 shadow-sm p-6">
        <h3 class="text-lg font-semibold text-gray-900 mb-6">
          Category Distribution
        </h3>

        <!-- Pie Chart -->
        <div class="flex justify-center">
          <CategoryDonut />
        </div>

        <!-- Legend (theme aligned, NO red) -->
        <div class="flex justify-center gap-8 text-sm text-gray-600 mt-6">
          <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-indigo-600"></span>
            <span>Income</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-blue-600"></span>
            <span>Expenses</span>
          </div>
          <div class="flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-slate-400"></span>
            <span>Uncategorized</span>
          </div>
        </div>
      </div>

      <!-- Summary Cards (Dashboard-style, fintech look) -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 w-full">

        <!-- Total Income -->
        <div class="bg-white border border-gray-100 rounded-2xl shadow-sm p-5">
          <p class="text-sm font-medium text-gray-500">
            Total Income
          </p>
          <p class="mt-2 text-2xl font-semibold text-indigo-600">
            ₹6,650.00
          </p>
        </div>

        <!-- Total Expenses (NO red) -->
        <div class="bg-white border border-gray-100 rounded-2xl shadow-sm p-5">
          <p class="text-sm font-medium text-gray-500">
            Total Expenses
          </p>
          <p class="mt-2 text-2xl font-semibold text-blue-600">
            ₹4,150.00
          </p>
        </div>

        <!-- Net Balance -->
        <div class="bg-white border border-gray-100 rounded-2xl shadow-sm p-5">
          <p class="text-sm font-medium text-gray-500">
            Net Balance
          </p>
          <p class="mt-2 text-2xl font-semibold text-violet-600">
            ₹2,500.00
          </p>
        </div>

      </div>

    </div>
  </template>
