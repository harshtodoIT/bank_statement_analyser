<script setup>
  import { useRouter } from 'vue-router'
  import { onMounted, ref } from 'vue'
  import {
    Utensils,
    Plane,
    ShoppingBag,
    Lightbulb,
    Car,
    Heart
  } from 'lucide-vue-next'

  const props = defineProps({
    name: String,
    amount: Number,
    percent: Number,
    icon: String,
    color: String // 'purple' | 'blue' | 'cyan' | 'gray'
  })
  const router = useRouter()


  const progress = ref(0)

  onMounted(() => {
    // animate progress bar
    setTimeout(() => {
      progress.value = props.percent
    }, 100)
  })

  const iconMap = {
    food: Utensils,
    travel: Plane,
    shopping: ShoppingBag,
    utilities: Lightbulb,
    transport: Car,
    healthcare: Heart
  }
  const goToCategoryDetails = () => {
  router.push(`/dashboard/category/${props.icon}`)
}

  </script>

  <template>
    <div
        class="bg-white border border-gray-100 rounded-2xl p-5 shadow-sm hover:shadow-md transition cursor-pointer"
        @click="goToCategoryDetails"
      >

      <!-- Top row -->
      <div class="flex items-center justify-between mb-4">
        <div class="flex items-center gap-3">
          <!-- Icon -->
          <div
            class="w-11 h-11 rounded-xl flex items-center justify-center"
            :class="{
              'bg-purple-100 text-purple-600': color === 'purple',
              'bg-blue-100 text-blue-600': color === 'blue',
              'bg-cyan-100 text-cyan-600': color === 'cyan',
              'bg-gray-100 text-gray-600': color === 'gray'
            }"
          >
            <component :is="iconMap[icon]" size="20" />
          </div>

          <!-- Name -->
          <p class="font-semibold text-gray-800">
            {{ name }}
          </p>
        </div>

        <!-- Percentage -->
        <p class="text-sm text-gray-500">
          {{ percent }}%
        </p>
      </div>

      <!-- Amount -->
      <p class="text-2xl font-bold text-gray-900 mb-4">
        ₹{{ amount.toLocaleString() }}
      </p>

      <!-- Progress bar -->
      <div class="h-2 bg-gray-100 rounded-full overflow-hidden">
        <div
          class="h-full rounded-full transition-all duration-700 ease-out"
          :class="{
            'bg-purple-500': color === 'purple',
            'bg-blue-500': color === 'blue',
            'bg-cyan-500': color === 'cyan',
            'bg-gray-400': color === 'gray'
          }"
          :style="{ width: progress + '%' }"
        ></div>
      </div>
    </div>
  </template>
