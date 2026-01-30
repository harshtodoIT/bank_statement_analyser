<script setup>
import { ref, computed, onMounted, onUnmounted } from "vue"
import { UserButton, useUser } from "@clerk/vue"

import {
  LayoutDashboard,
  PieChart,
  Calendar,
  SlidersHorizontal,
  Menu,
  ChevronLeft,
  History
} from "lucide-vue-next"

const props = defineProps({
  isOpen: Boolean
})

const emit = defineEmits(["toggle", "close-mobile"])

const isDesktop = ref(window.innerWidth >= 1024)

const handleResize = () => {
  isDesktop.value = window.innerWidth >= 1024
}

onMounted(() => window.addEventListener("resize", handleResize))
onUnmounted(() => window.removeEventListener("resize", handleResize))

const effectiveOpen = computed(() => {
  return isDesktop.value ? props.isOpen : true
})

const handleToggle = () => {
  if (window.innerWidth < 1024) {
    emit("close-mobile")
  } else {
    emit("toggle")
  }
}

const handleNavClick = () => {
  if (window.innerWidth < 1024) {
    emit("close-mobile")
  }
}

const exactActiveClass =
  "bg-indigo-500/20 text-indigo-400 shadow-[inset_3px_0_0_#6366F1]"

// Clerk user
const { user } = useUser()
const userButtonAppearance = {
  elements: {
    avatarBox: "w-9 h-9"
  }
}
</script>

<template>
  <div
    class="h-screen flex flex-col
           bg-gradient-to-b from-[#0B1220] to-[#111827]
           text-gray-300 border-r border-white/10
           transition-all duration-300"
    :class="[
      'w-[80vw] max-w-[280px]',
      effectiveOpen ? 'lg:w-64' : 'lg:w-20'
    ]"
  >

    <!-- HEADER -->
    <div class="h-16 px-4 flex items-center border-b border-white/10">
      <div
        class="flex-1 overflow-hidden transition-all duration-300"
        :class="effectiveOpen ? 'opacity-100 max-w-[180px]' : 'opacity-0 max-w-0'"
      >
        <span class="text-white font-semibold text-sm block">
          Bank Statement Analyzer
        </span>
        <span class="text-xs text-gray-400 block">
          Financial Dashboard
        </span>
      </div>

      <button
        @click="handleToggle"
        class="p-2 rounded-lg hover:bg-white/10 text-gray-300 transition"
      >
        <component :is="effectiveOpen ? ChevronLeft : Menu" size="20" />
      </button>
    </div>

    <!-- NAV -->
    <nav class="flex-1 px-3 py-4 space-y-2">

      <router-link
        to="/dashboard"
        :exact-active-class="exactActiveClass"
        @click="handleNavClick"
        class="group flex items-center px-3 py-2 rounded-lg
               transition-colors duration-200
               hover:bg-indigo-600 hover:text-white"
        :class="effectiveOpen ? 'gap-3 justify-start' : 'justify-center'"
      >
        <LayoutDashboard size="18" />
        <span
          class="transition-all duration-300 overflow-hidden"
          :class="effectiveOpen ? 'opacity-100 w-auto' : 'opacity-0 w-0'"
        >
          Dashboard
        </span>
      </router-link>

      <router-link
        to="/dashboard/category-breakdown"
        :exact-active-class="exactActiveClass"
        @click="handleNavClick"
        class="group flex items-center px-3 py-2 rounded-lg
               transition-colors duration-200
               hover:bg-indigo-600 hover:text-white"
        :class="effectiveOpen ? 'gap-3 justify-start' : 'justify-center'"
      >
        <PieChart size="18" />
        <span
          class="transition-all duration-300 overflow-hidden"
          :class="effectiveOpen ? 'opacity-100 w-auto' : 'opacity-0 w-0'"
        >
          Category Breakdown
        </span>
      </router-link>

      <router-link
        to="/dashboard/monthly-summary"
        :exact-active-class="exactActiveClass"
        @click="handleNavClick"
        class="group flex items-center px-3 py-2 rounded-lg
               transition-colors duration-200
               hover:bg-indigo-600 hover:text-white"
        :class="effectiveOpen ? 'gap-3 justify-start' : 'justify-center'"
      >
        <Calendar size="18" />
        <span
          class="transition-all duration-300 overflow-hidden"
          :class="effectiveOpen ? 'opacity-100 w-auto' : 'opacity-0 w-0'"
        >
          Monthly Summary
        </span>
      </router-link>

      <router-link
        to="/dashboard/manual-adjustment"
        :exact-active-class="exactActiveClass"
        @click="handleNavClick"
        class="group flex items-center px-3 py-2 rounded-lg
               transition-colors duration-200
               hover:bg-indigo-600 hover:text-white"
        :class="effectiveOpen ? 'gap-3 justify-start' : 'justify-center'"
      >
        <SlidersHorizontal size="18" />
        <span
          class="transition-all duration-300 overflow-hidden"
          :class="effectiveOpen ? 'opacity-100 w-auto' : 'opacity-0 w-0'"
        >
          Manual Adjustment
        </span>
      </router-link>

      <router-link
        to="/dashboard/history"
        :exact-active-class="exactActiveClass"
        @click="handleNavClick"
        class="group flex items-center px-3 py-2 rounded-lg
               transition-colors duration-200
               hover:bg-indigo-600 hover:text-white"
        :class="effectiveOpen ? 'gap-3 justify-start' : 'justify-center'"
      >
        <History size="18" />
        <span
          class="transition-all duration-300 overflow-hidden"
          :class="effectiveOpen ? 'opacity-100 w-auto' : 'opacity-0 w-0'"
        >
          History
        </span>
      </router-link>

    </nav>

    <!-- USER (CLERK) -->
    <div class="p-4 border-t border-white/10">
      <div class="flex items-center gap-3">

        <!-- Avatar / Button -->
        <UserButton :appearance="userButtonAppearance" />


        <!-- User info (only when expanded) -->
        <div
          class="overflow-hidden transition-all duration-300"
          :class="effectiveOpen ? 'opacity-100 max-w-[180px]' : 'opacity-0 max-w-0'"
        >
          <p class="text-sm font-medium text-white">
            {{ user?.fullName || "User" }}
          </p>
          <p class="text-xs text-gray-400">
            {{ user?.primaryEmailAddress?.emailAddress }}
          </p>
        </div>

      </div>
    </div>

  </div>
</template>
