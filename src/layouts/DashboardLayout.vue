<script setup>
  import { ref } from "vue"
  import { useRoute } from "vue-router"

  import DashboardHeader from "../components/dashboard/DashboardHeader.vue"
  import DashboardSidebar from "../components/dashboard/DashboardSidebar.vue"

  const route = useRoute()

  const desktopOpen = ref(true)
  const mobileOpen = ref(false)

  const toggleDesktop = () => {
    desktopOpen.value = !desktopOpen.value
  }

  const toggleMobile = () => {
    mobileOpen.value = !mobileOpen.value
  }

  const closeMobile = () => {
    mobileOpen.value = false
  }
  </script>


<template>
  <div class="flex h-screen bg-gray-50 overflow-hidden">

    <!-- Sidebar -->
    <div
      class="fixed inset-y-0 left-0 z-40 transform transition-transform duration-300
             lg:static lg:translate-x-0"
      :class="mobileOpen ? 'translate-x-0' : '-translate-x-full'"
    >
      <DashboardSidebar
        :isOpen="desktopOpen"
        @toggle="toggleDesktop"
        @click="closeMobile"
      />
    </div>

    <!-- Overlay -->
    <div
      v-if="mobileOpen"
      class="fixed inset-0 bg-black/40 z-30 lg:hidden"
      @click="closeMobile"
    />

    <!-- Main -->
    <div class="flex-1 flex flex-col overflow-hidden">

      <!-- MOBILE HEADER (ALL PAGES) -->
      <header class="lg:hidden bg-white border-b px-4 py-3">
        <div class="flex items-start gap-3">
          <button
            class="p-2 rounded hover:bg-gray-100"
            @click="toggleMobile"
          >
            ☰
          </button>

          <div>
            <!-- Dashboard title only on dashboard -->
            <h1
              v-if="route.path === '/dashboard'"
              class="text-xl font-bold text-gray-900"
            >
              Dashboard
            </h1>
            <p class="text-sm text-gray-500">
              Bank Statement Analyzer
            </p>
          </div>
        </div>
      </header>

      <!-- DESKTOP DASHBOARD HEADER ONLY -->
      <DashboardHeader
          v-if="route.path === '/dashboard'"
          class="hidden lg:block"
          @toggle="toggleDesktop"
        />


      <!-- Page content -->
      <main class="flex-1 overflow-y-auto p-4 sm:p-5 lg:p-6">
        <router-view />
      </main>

    </div>
  </div>
</template>

