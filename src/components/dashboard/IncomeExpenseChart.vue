<script setup>
  import { computed, ref, onMounted } from "vue"
  import { useDashboardStore } from "../../stores/dashboard.store"
  
  const dashboardStore = useDashboardStore()
  const animated = ref(false)
  
  const months = computed(() => {
    return Object.entries(dashboardStore.monthlySummary || {}).map(
      ([month, values]) => ({
        name: month,
        income: values.income,
        expense: values.expense,
      })
    )
  })
  
  const maxValue = computed(() => {
    const all = months.value.flatMap(m => [m.income, m.expense])
    return Math.max(...all, 1)
  })
  
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
  
      <div v-if="!months.length" class="text-sm text-gray-500">
        No monthly data available
      </div>
  
      <div v-else class="overflow-x-auto lg:overflow-x-hidden">
        <div class="relative flex min-w-[640px]">
  
          <!-- Y Axis -->
          <div class="flex flex-col justify-between h-[220px] pr-4 text-sm text-gray-400 shrink-0">
            <span>₹{{ maxValue }}</span>
            <span>₹{{ Math.round(maxValue * 0.75) }}</span>
            <span>₹{{ Math.round(maxValue * 0.5) }}</span>
            <span>₹{{ Math.round(maxValue * 0.25) }}</span>
            <span>₹0</span>
          </div>
  
          <!-- Chart -->
          <div class="relative flex-1">
            <div class="absolute inset-0 flex flex-col justify-between">
              <div
                v-for="i in 5"
                :key="i"
                class="border-t border-dashed border-gray-200"
              ></div>
            </div>
  
            <div class="relative flex items-end h-[220px] gap-6 px-4">
              <div
                v-for="month in months"
                :key="month.name"
                class="flex flex-col items-center w-[72px]"
              >
                <div class="flex items-end gap-2 h-full">
                  <div
                    class="w-6 bg-green-600 rounded-md transition-all duration-700"
                    :style="{
                      height: animated
                        ? (month.income / maxValue) * chartHeight + 'px'
                        : '0px'
                    }"
                  ></div>
  
                  <div
                    class="w-6 bg-blue-800 rounded-md transition-all duration-700"
                    :style="{
                      height: animated
                        ? (month.expense / maxValue) * chartHeight + 'px'
                        : '0px'
                    }"
                  ></div>
                </div>
  
                <span class="mt-3 text-sm text-gray-500">
                  {{ month.name }}
                </span>
              </div>
            </div>
  
            <div class="absolute bottom-[28px] left-0 right-0 border-t border-gray-300"></div>
          </div>
        </div>
      </div>
  
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
  