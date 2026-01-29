<script setup>
import { useRouter } from "vue-router"
import { onMounted, ref } from "vue"
import {
  Utensils,
  Plane,
  ShoppingBag,
  Lightbulb,
  Car,
  Heart,
  Wallet
} from "lucide-vue-next"

const props = defineProps({
  name: String,
  amount: Number,
  percent: Number,
  icon: String,
  color: String
})

const router = useRouter()
const progress = ref(0)

onMounted(() => {
  setTimeout(() => {
    progress.value = props.percent || 0
  }, 100)
})

const iconMap = {
  food: Utensils,
  travel: Plane,
  shopping: ShoppingBag,
  utilities: Lightbulb,
  transport: Car,
  healthcare: Heart,
  income: Wallet,
  expense: Wallet,
  uncategorized: Wallet
}

const goToCategoryDetails = () => {
  router.push(`/dashboard/category/${encodeURIComponent(props.name)}`)
}
</script>

<template>
  <div
    class="bg-slate-800 border border-white/10 rounded-2xl p-5
           transition cursor-pointer
           hover:bg-slate-700/70 hover:-translate-y-0.5"
    @click="goToCategoryDetails"
  >
    <div class="flex items-center justify-between mb-4">
      <div class="flex items-center gap-3">
        <div
          class="w-11 h-11 rounded-xl flex items-center justify-center"
          :class="{
            'bg-purple-500/20 text-purple-400': color === 'purple',
            'bg-blue-500/20 text-blue-400': color === 'blue',
            'bg-cyan-500/20 text-cyan-400': color === 'cyan',
            'bg-slate-500/20 text-slate-400': color === 'gray',
            'bg-green-500/20 text-green-400': color === 'green',
            'bg-indigo-500/20 text-indigo-400': color === 'indigo'
          }"
        >
          <component :is="iconMap[icon] || Wallet" size="20" />
        </div>

        <p class="font-semibold text-white">
          {{ name }}
        </p>
      </div>

      <p class="text-sm text-slate-400">
        {{ percent }}%
      </p>
    </div>

    <p class="text-2xl font-bold text-white mb-4">
      ₹{{ amount.toLocaleString() }}
    </p>

    <div class="h-2 bg-white/10 rounded-full overflow-hidden">
      <div
        class="h-full rounded-full transition-all duration-700 ease-out"
        :class="{
          'bg-purple-400': color === 'purple',
          'bg-blue-400': color === 'blue',
          'bg-cyan-400': color === 'cyan',
          'bg-slate-400': color === 'gray',
          'bg-green-400': color === 'green',
          'bg-indigo-400': color === 'indigo'
        }"
        :style="{ width: progress + '%' }"
      />
    </div>
  </div>
</template>
