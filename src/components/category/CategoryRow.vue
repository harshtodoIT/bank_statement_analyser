<script setup>
  import { computed } from "vue";

  const props = defineProps({
    name: String,
    amount: Number,
    total: Number,
    type: String
  });

  const percentage = computed(() =>
    props.total ? Math.round((props.amount / props.total) * 100) : 0
  );
  </script>

  <template>
    <div class="border rounded-lg p-4 space-y-3">
      <!-- Header -->
      <div class="flex justify-between items-center">
        <div class="flex items-center gap-3">
          <div
            class="w-9 h-9 rounded-lg flex items-center justify-center"
            :class="{
              'bg-green-100 text-green-600': type === 'income',
              'bg-red-100 text-red-600': type === 'expense',
              'bg-orange-100 text-orange-600': type === 'uncategorized'
            }"
          >
            ●
          </div>

          <p class="font-medium text-gray-800">
            {{ name }}
          </p>
        </div>

        <div class="text-right">
          <p class="font-medium">₹{{ amount.toLocaleString() }}</p>
          <p class="text-xs text-gray-500">{{ percentage }}%</p>
        </div>
      </div>

      <!-- Progress bar -->
      <div class="h-2 bg-gray-200 rounded-full overflow-hidden">
        <div
          class="h-full rounded-full transition-all duration-500"
          :style="{ width: percentage + '%' }"
          :class="{
            'bg-green-500': type === 'income',
            'bg-red-500': type === 'expense',
            'bg-orange-500': type === 'uncategorized'
          }"
        ></div>
      </div>
    </div>
  </template>
