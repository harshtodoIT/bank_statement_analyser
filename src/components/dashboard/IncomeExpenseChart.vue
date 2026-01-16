<script setup>
  import { computed, ref, onMounted } from "vue";
  import { useDashboardStore } from "../../stores/dashboard.store";

  const dashboardStore = useDashboardStore();
  const animated = ref(false);

  const months = computed(() =>
    Object.entries(dashboardStore.monthlySummary || {}).map(
      ([name, values]) => ({
        name,
        income: values?.income || 0,
        expense: values?.expense || 0
      })
    )
  );

  const maxValue = computed(() => {
    const vals = months.value.flatMap(m => [m.income, m.expense]);
    return Math.max(...vals, 1);
  });

  const chartHeight = 220;

  onMounted(() => {
    setTimeout(() => {
      animated.value = true;
    }, 100);
  });
  </script>

  <template>
    <div class="bg-white rounded-2xl p-6 shadow-sm">
      <h2 class="text-lg font-semibold mb-6">
        Income vs Expenses Overview
      </h2>

      <div class="relative flex">
        <!-- Y Axis -->
        <div class="flex flex-col justify-between h-[220px] pr-4 text-sm text-gray-400">
          <span>₹{{ (maxValue).toFixed(0) }}</span>
          <span>₹{{ (maxValue * 0.75).toFixed(0) }}</span>
          <span>₹{{ (maxValue * 0.5).toFixed(0) }}</span>
          <span>₹{{ (maxValue * 0.25).toFixed(0) }}</span>
          <span>₹0</span>
        </div>

        <!-- Chart Area -->
        <div class="relative flex-1">
          <div class="absolute inset-0 flex flex-col justify-between">
            <div
              v-for="i in 5"
              :key="i"
              class="border-t border-dashed border-gray-200"
            ></div>
          </div>

          <div class="relative flex justify-between items-end h-[220px] px-2">
            <div
              v-for="m in months"
              :key="m.name"
              class="flex flex-col items-center w-full"
            >
              <div class="flex items-end gap-2 h-full">
                <!-- Income -->
                <div
                  class="w-6 bg-green-600 rounded-md transition-all duration-700"
                  :style="{
                    height: animated
                      ? (m.income / maxValue) * chartHeight + 'px'
                      : '0px'
                  }"
                ></div>

                <!-- Expense -->
                <div
                  class="w-6 bg-red-600 rounded-md transition-all duration-700"
                  :style="{
                    height: animated
                      ? (m.expense / maxValue) * chartHeight + 'px'
                      : '0px'
                  }"
                ></div>
              </div>

              <span class="mt-3 text-sm text-gray-500">
                {{ m.name }}
              </span>
            </div>
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
          <span class="w-3 h-3 rounded-full bg-red-600"></span>
          Expenses
        </div>
      </div>
    </div>
  </template>
