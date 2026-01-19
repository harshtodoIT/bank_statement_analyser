<template>
  <!-- Dashboard Header -->
  <div class="bg-white border-b border-gray-200 px-6 py-4">
    <div class="flex items-center justify-between">

      <!-- Left: Title -->
      <div>
        <h1 class="text-2xl font-semibold text-gray-900">
          Dashboard
        </h1>
        <p class="text-sm text-gray-500 mt-1">
          Financial insights and analytics dashboard
        </p>
      </div>

      <!-- Right: Export Button -->
      <button
        class="flex items-center gap-2 bg-indigo-600 hover:bg-indigo-700
               text-white px-4 py-2 rounded-lg shadow-sm transition"
      >
        <!-- Icon -->
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="w-4 h-4"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="M12 16v-8m0 0l-4 4m4-4l4 4M4 20h16" />
        </svg>

        <span class="text-sm font-medium">Export Report</span>
      </button>

    </div>
  </div>
</template>
