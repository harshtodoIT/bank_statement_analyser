<script setup>
  import { ref } from "vue"
  // import { useRoute } from "vue-router"

  import DashboardSidebar from "../components/dashboard/DashboardSidebar.vue"

  // const route = useRoute()

  const desktopOpen = ref(true)
  const mobileOpen = ref(false)

  const toggleDesktop = () => {
    desktopOpen.value = !desktopOpen.value
  }

  const toggleMobile = () => {
  // Always open sidebar in expanded mode on mobile
  desktopOpen.value = true
  mobileOpen.value = !mobileOpen.value
}


  const closeMobile = () => {
  mobileOpen.value = false
  // keep desktop state unchanged
}

  </script>


<template>
  <div class="flex h-screen bg-slate-900 overflow-hidden">

    <!-- Sidebar -->
    <div
      class="fixed inset-y-0 left-0 z-40 transform transition-transform duration-300
             lg:static lg:translate-x-0"
      :class="mobileOpen ? 'translate-x-0' : '-translate-x-full'"
    >
          <DashboardSidebar
        :isOpen="desktopOpen"
        @toggle="toggleDesktop"
        @close-mobile="closeMobile"
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
      <header class="lg:hidden bg-slate-900 border-b border-white/10 px-4 py-3">
        <div class="flex items-start gap-3">
          <button
          class="p-2 rounded text-slate-200 hover:text-white hover:bg-white/10 transition"
          @click="toggleMobile"
        >
          ☰
        </button>



          <div>
            <p class="text-2xl font-bold text-white">
              Bank Statement Analyzer
            </p>
          </div>
        </div>
      </header>

      <!-- Page content -->
      <main class="flex-1 overflow-y-auto p-4 sm:p-5 lg:p-6 text-gray-100">
        <router-view />
      </main>

    </div>
  </div>
</template>

