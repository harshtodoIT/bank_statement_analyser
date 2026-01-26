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
    class="bg-slate-800 border border-white/10 rounded-2xl p-5
           transition cursor-pointer
           hover:bg-slate-700/70 hover:-translate-y-0.5"
    @click="goToCategoryDetails"
  >

    <!-- ================= Top row ================= -->
    <div class="flex items-center justify-between mb-4">
      <div class="flex items-center gap-3">

        <!-- Icon -->
        <div
          class="w-11 h-11 rounded-xl flex items-center justify-center"
          :class="{
            'bg-purple-500/20 text-purple-400': color === 'purple',
            'bg-blue-500/20 text-blue-400': color === 'blue',
            'bg-cyan-500/20 text-cyan-400': color === 'cyan',
            'bg-slate-500/20 text-slate-400': color === 'gray'
          }"
        >
          <component :is="iconMap[icon]" size="20" />
        </div>

        <!-- Name -->
        <p class="font-semibold text-white">
          {{ name }}
        </p>
      </div>

      <!-- Percentage -->
      <p class="text-sm text-slate-400">
        {{ percent }}%
      </p>
    </div>

    <!-- ================= Amount ================= -->
    <p class="text-2xl font-bold text-white mb-4">
      ₹{{ amount.toLocaleString() }}
    </p>

    <!-- ================= Progress bar ================= -->
    <div class="h-2 bg-white/10 rounded-full overflow-hidden">
      <div
        class="h-full rounded-full transition-all duration-700 ease-out"
        :class="{
          'bg-purple-400': color === 'purple',
          'bg-blue-400': color === 'blue',
          'bg-cyan-400': color === 'cyan',
          'bg-slate-400': color === 'gray'
        }"
        :style="{ width: progress + '%' }"
      ></div>
    </div>

  </div>
</template>
