<script setup>
  import { ref } from 'vue'
  import DashboardSidebar from '../components/dashboard/DashboardSidebar.vue'

  const isOpen = ref(true)
  </script>

  <template>
    <div class="flex h-screen bg-gray-50">

      <!-- Sidebar -->
      <aside
  class="sticky top-0 h-screen bg-gray-50 border-r border-gray-200
         transition-all duration-300"
>

        <DashboardSidebar
          :isOpen="isOpen"
          @toggle="isOpen = !isOpen"
        />
      </aside>

      <!-- Main Content -->
      <main class="flex-1 overflow-y-auto relative z-10">
        <router-view />
      </main>

    </div>
  </template>
