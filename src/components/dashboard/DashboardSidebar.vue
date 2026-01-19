<script setup>
  import { useRoute } from 'vue-router'
  import SidebarItem from './SidebarItem.vue'

  import {
    LayoutDashboard,
    PieChart,
    Calendar,
    FileText,
    SlidersHorizontal,
    Menu,
    ChevronLeft
  } from 'lucide-vue-next'

  defineProps({
    isOpen: Boolean
  })

  const emit = defineEmits(['toggle'])
  const route = useRoute()
  </script>

  <template>
    <div
          class="h-full flex flex-col
         bg-gradient-to-b from-[#0b1220] to-[#111827]
         text-gray-300 border-r border-white/10
         transition-all duration-300 ease-in-out"
          :class="isOpen ? 'w-[260px]' : 'w-[80px]'"
    >


      <!-- HEADER -->
      <div class="h-16 px-4 flex items-center justify-between border-b border-white/10">

        <!-- Expanded -->
        <div v-if="isOpen" class="flex flex-col">
          <span class="text-white font-semibold text-sm">
            Statement Analyzer
          </span>
          <span class="text-xs text-gray-400">
            Financial Dashboard
          </span>
        </div>

        <!-- Toggle -->
        <button
          @click="emit('toggle')"
          class="p-2 rounded-lg hover:bg-white/10 text-gray-300"
        >
          <component :is="isOpen ? ChevronLeft : Menu" size="20" />
        </button>
      </div>

      <!-- NAVIGATION -->
      <nav class="flex-1 px-3 py-4 space-y-2">

        <!-- Dashboard -->
        <SidebarItem label="Dashboard" :isOpen="isOpen">
          <router-link
            to="/dashboard"
            class="nav-item"
            :class="{ active: route.path === '/dashboard' }"
          >
            <LayoutDashboard size="18" />
            <span v-if="isOpen">Dashboard</span>
          </router-link>
        </SidebarItem>

        <!-- Category -->
        <SidebarItem label="Category Breakdown" :isOpen="isOpen">
          <router-link
            to="/dashboard/category-breakdown"
            class="nav-item"
            :class="{ active: route.path === '/dashboard/category-breakdown' }"
          >
            <PieChart size="18" />
            <span v-if="isOpen">Category Breakdown</span>
          </router-link>
        </SidebarItem>

        <!-- Monthly -->
        <SidebarItem label="Monthly Summary" :isOpen="isOpen">
          <router-link
            to="/dashboard/monthly-summary"
            class="nav-item"
            :class="{ active: route.path.includes('monthly-summary') }"
          >
            <Calendar size="18" />
            <span v-if="isOpen">Monthly Summary</span>
          </router-link>
        </SidebarItem>

        <!-- Reports -->
        <SidebarItem label="Reports" :isOpen="isOpen">
          <router-link
            to="/dashboard/reports"
            class="nav-item"
            :class="{ active: route.path.includes('reports') }"
          >
            <FileText size="18" />
            <span v-if="isOpen">Reports</span>
          </router-link>
        </SidebarItem>

        <!-- Manual -->
        <SidebarItem label="Manual Adjustment" :isOpen="isOpen">
          <router-link
            to="/dashboard/manual-adjustment"
            class="nav-item"
            :class="{ active: route.path.includes('manual-adjustment') }"
          >
            <SlidersHorizontal size="18" />
            <span v-if="isOpen">Manual Adjustment</span>
          </router-link>
        </SidebarItem>

      </nav>

      <!-- USER SECTION -->
      <div class="p-4 border-t border-white/10">

        <!-- Expanded -->
        <div v-if="isOpen" class="space-y-3">
          <div class="flex items-center gap-3">
            <div class="w-9 h-9 rounded-full bg-white/10 flex items-center justify-center">
              👤
            </div>
            <div>
              <p class="text-sm font-medium text-white">Guest User</p>
              <p class="text-xs text-gray-400">Temporary session</p>
            </div>
          </div>

          <button
            class="w-full bg-indigo-600 hover:bg-indigo-700
                   text-white text-sm py-2 rounded-lg transition"
          >
            Login to save data permanently
          </button>
        </div>

        <!-- Collapsed -->
        <div v-else class="flex justify-center">
          <div class="w-9 h-9 rounded-full bg-white/10 flex items-center justify-center">
            👤
          </div>
        </div>

      </div>
    </div>
  </template>

  <style scoped>
  .nav-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0 0.75rem;
    height: 2.75rem;
    border-radius: 0.75rem;
    color: #d1d5db;
    transition: all 0.2s ease;
    position: relative;
  }

  .nav-item:hover {
    background-color: rgba(255, 255, 255, 0.06);
  }

  .nav-item svg {
    color: #9ca3af;
  }

  /* ACTIVE ITEM (PURPLE PILL) */
  .nav-item.active {
    background: linear-gradient(90deg, #6366f1, #7c3aed);
    color: #ffffff;
    font-weight: 500;
    box-shadow: 0 8px 20px rgba(99, 102, 241, 0.35);
  }

  .nav-item.active svg {
    color: #ffffff;
  }
  </style>
