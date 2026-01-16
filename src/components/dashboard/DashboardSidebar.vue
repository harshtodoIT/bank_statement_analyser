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
    <div class="h-full flex flex-col bg-white border-r">

      <!-- HEADER -->
      <div class="h-16 px-4 flex items-center justify-between border-b">

        <!-- Expanded -->
        <div v-if="isOpen" class="flex items-center gap-3">
          
          <span class="font-semibold text-gray-800">
            Bank Statement Analyser
          </span>
        </div>

        <!-- Collapsed -->


        <!-- Toggle -->
        <button
          @click="emit('toggle')"
          class="p-2 rounded-lg hover:bg-gray-100"
        >
          <component :is="isOpen ? ChevronLeft : Menu" size="20" />
        </button>
      </div>

      <!-- NAVIGATION -->
      <nav class="flex-1 px-3 py-4 space-y-1">

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
      <div class="p-4 border-t">

        <!-- Expanded -->
        <div v-if="isOpen" class="space-y-3">
          <div class="flex items-center gap-3">
            <div class="w-9 h-9 rounded-full bg-gray-200 flex items-center justify-center">
              👤
            </div>
            <div>
              <p class="text-sm font-medium">Guest User</p>
              <p class="text-xs text-gray-500">Temporary session</p>
            </div>
          </div>

          <button class="w-full bg-blue-600 text-white text-sm py-2 rounded-lg">
            Login to save data permanently
          </button>
        </div>

        <!-- Collapsed -->
        <div v-else class="flex justify-center">
          <div class="w-9 h-9 rounded-full bg-gray-200 flex items-center justify-center">
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
    color: #374151;
    transition: background-color 0.15s ease-in-out;
    position: relative;
  }

  .nav-item:hover {
    background-color: #f3f4f6;
  }

  .nav-item svg {
    color: #6b7280;
  }

  .nav-item.active {
    background-color: #eff6ff;
    color: #2563eb;
    font-weight: 500;
  }

  .nav-item.active svg {
    color: #2563eb;
  }

  .nav-item.active::before {
    content: '';
    position: absolute;
    left: 0;
    top: 50%;
    transform: translateY(-50%);
    width: 0.25rem;
    height: 1.5rem;
    background-color: #2563eb;
    border-radius: 0 0.25rem 0.25rem 0;
  }
  </style>
