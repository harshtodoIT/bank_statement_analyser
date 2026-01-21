<script setup>
  import { ref, onMounted } from 'vue'

  const animated = ref(false)

  const months = [
    { name: 'Jan', income: 7200, expense: 5400 },
    { name: 'Feb', income: 6800, expense: 4900 },
    { name: 'Mar', income: 8000, expense: 5800 },
    { name: 'Apr', income: 7500, expense: 5100 },
    { name: 'May', income: 7900, expense: 5600 },
    { name: 'Jun', income: 7700, expense: 5300 }
  ]

  const maxValue = 10000
  const chartHeight = 220

  onMounted(() => {
    setTimeout(() => {
      animated.value = true
    }, 100)
  })
  </script>

  <template>
    <div class="bg-white rounded-2xl p-6 shadow-sm">
      <h2 class="text-lg font-semibold mb-6">
        Income vs Expenses Overview
      </h2>

      <!-- ✅ Scroll wrapper (mobile only) -->
      <div class="overflow-x-auto lg:overflow-x-hidden scrollbar-hide">
        <div class="relative flex min-w-[640px]">

          <!-- Y Axis -->
          <div class="flex flex-col justify-between h-[220px] pr-4 text-sm text-gray-400 shrink-0">
            <span>₹10k</span>
            <span>₹7.5k</span>
            <span>₹5k</span>
            <span>₹2.5k</span>
            <span>₹0k</span>
          </div>

          <!-- Chart Area -->
          <div class="relative flex-1">

            <!-- Grid Lines -->
            <div class="absolute inset-0 flex flex-col justify-between">
              <div
                v-for="i in 5"
                :key="i"
                class="border-t border-dashed border-gray-200"
              ></div>
            </div>

            <!-- Bars -->
            <div class="relative flex items-end h-[220px] gap-6 px-4">

              <div
                v-for="month in months"
                :key="month.name"
                class="flex flex-col items-center w-[72px]"
              >
                <div class="flex items-end gap-2 h-full">

                  <!-- Income -->
                  <div
                    class="w-6 bg-green-600 rounded-md transition-all duration-700 ease-out"
                    :style="{
                      height: animated
                        ? (month.income / maxValue) * chartHeight + 'px'
                        : '0px'
                    }"
                  ></div>

                  <!-- Expense -->
                  <div
                    class="w-6 bg-blue-800 rounded-md transition-all duration-700 ease-out"
                    :style="{
                      height: animated
                        ? (month.expense / maxValue) * chartHeight + 'px'
                        : '0px'
                    }"
                  ></div>

                </div>

                <!-- Month -->
                <span class="mt-3 text-sm text-gray-500">
                  {{ month.name }}
                </span>
              </div>

            </div>

            <!-- X-axis -->
            <div class="absolute bottom-[28px] left-0 right-0 border-t border-gray-300"></div>

          </div>
        </div>
      </div>

      <!-- Legend -->
      <div class="flex justify-center gap-6 mt-6 text-sm text-gray-600">
        <div class="flex items-center gap-2">
          <span class="w-3 h-3 rounded-full bg-green-600"></span>
          Income
        </div>
        <div class="flex items-center gap-2">
          <span class="w-3 h-3 rounded-full bg-blue-800"></span>
          Expenses
        </div>
      </div>
    </div>
  </template>
