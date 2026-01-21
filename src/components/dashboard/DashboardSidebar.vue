<script setup>
  // import { useRoute } from 'vue-router'

  import {
    LayoutDashboard,
    PieChart,
    Calendar,
    SlidersHorizontal,
    Menu,
    ChevronLeft
  } from 'lucide-vue-next'

  defineProps({
    isOpen: Boolean
  })

  const emit = defineEmits(['toggle'])
  // const route = useRoute()
  </script>

  <template>
  <div
    class="h-screen flex flex-col
          bg-gradient-to-b from-[#0b1220] to-[#111827]
          text-gray-300 border-r border-white/10
          transition-all duration-300"
        :class="[
        'w-[80vw] max-w-[280px]',
        isOpen ? 'lg:w-64' : 'lg:w-20'
      ]"
  >




      <!-- HEADER -->
<div class="h-16 px-4 flex items-center border-b border-white/10">

<!-- Text -->
<div
  class="flex-1 overflow-hidden transition-all duration-300"
  :class="isOpen ? 'opacity-100 max-w-[180px]' : 'opacity-0 max-w-0'"
>
  <span class="text-white font-semibold text-sm block">
    Bank Statement Analyzer
  </span>
  <span class="text-xs text-gray-400 block">
    Financial Dashboard
  </span>
</div>

<!-- Toggle -->
<button
  @click="emit('toggle')"
  class="p-2 rounded-lg hover:bg-white/10 text-gray-300 transition"
>
  <component :is="isOpen ? ChevronLeft : Menu" size="20" />
</button>

</div>

      <!-- NAV -->
      <nav class="flex-1 px-3 py-4 space-y-2">

        <router-link
          to="/dashboard"
          class="flex items-center px-3 py-2 rounded-lg
       transition-colors duration-200
       hover:bg-indigo-600 hover:text-white"
:class="isOpen ? 'gap-3 justify-start' : 'justify-center'"


        >
          <LayoutDashboard size="18" />
          <span
  class="whitespace-nowrap overflow-hidden transition-all duration-300"
  :class="isOpen
    ? 'opacity-100 translate-x-0 max-w-[160px]'
    : 'opacity-0 -translate-x-2 max-w-0'"
>
  Dashboard
</span>

        </router-link>

        <router-link
          to="/dashboard/category-breakdown"
          class="flex items-center px-3 py-2 rounded-lg
       transition-colors duration-200
       hover:bg-indigo-600 hover:text-white"
:class="isOpen ? 'gap-3 justify-start' : 'justify-center'"

        >
          <PieChart size="18" />
          <span class="whitespace-nowrap transition-all duration-300 overflow-hidden"
  :class="isOpen
    ? 'opacity-100 translate-x-0 w-auto'
    : 'opacity-0 -translate-x-2 w-0'">Category Breakdown</span>
        </router-link>

        <router-link
          to="/dashboard/monthly-summary"
          class="flex items-center px-3 py-2 rounded-lg
       transition-colors duration-200
       hover:bg-indigo-600 hover:text-white"
:class="isOpen ? 'gap-3 justify-start' : 'justify-center'"

        >
          <Calendar size="18" />
          <span class="whitespace-nowrap transition-all duration-300 overflow-hidden"
  :class="isOpen
    ? 'opacity-100 translate-x-0 w-auto'
    : 'opacity-0 -translate-x-2 w-0'">Monthly Summary</span>
        </router-link>


        <router-link
            to="/dashboard/manual-adjustment"
                  class="flex items-center px-3 py-2 rounded-lg
                transition-colors duration-200
                  hover:bg-indigo-600 hover:text-white"
                :class="isOpen ? 'gap-3 justify-start' : 'justify-center'"

            >
  <SlidersHorizontal size="18" />
  <span class="whitespace-nowrap transition-all duration-300 overflow-hidden"
  :class="isOpen
    ? 'opacity-100 translate-x-0 w-auto'
    : 'opacity-0 -translate-x-2 w-0'">Manual Adjustment</span>
</router-link>

      </nav>

      <!-- USER -->
<!-- USER -->
<div class="p-4 border-t border-white/10">

<div class="flex items-center gap-3">

  <!-- Avatar (ALWAYS visible) -->
  <div class="w-9 h-9 rounded-full bg-white/10 flex items-center justify-center shrink-0">
    👤
  </div>

  <!-- Text (animated) -->
  <div
    class="overflow-hidden transition-all duration-300"
    :class="isOpen ? 'opacity-100 max-w-[180px]' : 'opacity-0 max-w-0'"
  >
    <p class="text-sm font-medium text-white">Guest User</p>
    <p class="text-xs text-gray-400 mb-1">Temporary session</p>

    <button
      class="w-full bg-indigo-600 hover:bg-indigo-700
             text-white text-xs py-1.5 rounded-md transition"
    >
      Login
    </button>
  </div>

</div>
</div>
</div>
</template>

