<script setup>
  import { ref } from 'vue'

  const showDropdown = ref(false)

  function toggleDropdown() {
    showDropdown.value = !showDropdown.value
  }

  function handleDownload(type) {
    console.log('Download requested:', type)
    showDropdown.value = false
  }
  </script>

  <template>
    <!-- Card wrapper -->
    <div class="bg-white rounded-2xl p-6 shadow-sm border border-gray-100 relative">
      <!-- Title -->
      <h3 class="text-lg font-semibold text-gray-900">
        Export Reports
      </h3>

      <!-- Subtitle -->
      <p class="mt-2 text-sm text-gray-500">
        Download your financial analysis in different formats
      </p>

      <!-- Download button -->
      <button
        @click="toggleDropdown"
        class="mt-6 w-full flex items-center justify-center gap-3
               bg-blue-600 hover:bg-blue-700
               text-white font-semibold
               py-3 rounded-xl transition"
      >
        <!-- Download icon -->
        <svg
          class="w-5 h-5"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M12 3v12m0 0l4-4m-4 4l-4-4M4 17h16"
          />
        </svg>

        Download Report

        <!-- Chevron -->
        <svg
          class="w-4 h-4"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M19 9l-7 7-7-7"
          />
        </svg>
      </button>

      <!-- Dropdown (FLOATING, does not affect layout) -->
      <div
        v-if="showDropdown"
        class="absolute left-6 right-6 top-[170px]
               bg-white border border-gray-200
               rounded-xl shadow-xl z-50 overflow-hidden"
      >
        <!-- PDF -->
        <button
          @click="handleDownload('pdf')"
          class="w-full flex gap-3 px-4 py-3 hover:bg-gray-50 text-left"
        >
          <svg
            class="w-6 h-6 text-red-600"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M7 7h10M7 11h10M7 15h6M5 3h10l4 4v14H5z"
            />
          </svg>

          <div>
            <p class="font-medium text-gray-900">PDF Report</p>
            <p class="text-sm text-gray-500">
              Complete analysis with charts
            </p>
          </div>
        </button>

        <!-- Divider -->
        <div class="border-t border-gray-100"></div>

        <!-- CSV -->
        <button
          @click="handleDownload('csv')"
          class="w-full flex gap-3 px-4 py-3 hover:bg-gray-50 text-left"
        >
          <svg
            class="w-6 h-6 text-green-600"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M7 7h10M7 11h10M7 15h6M5 3h10l4 4v14H5z"
            />
          </svg>

          <div>
            <p class="font-medium text-gray-900">CSV Export</p>
            <p class="text-sm text-gray-500">
              Raw transaction data
            </p>
          </div>
        </button>
      </div>
    </div>
  </template>
