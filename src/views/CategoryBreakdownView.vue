<script setup>
import { computed } from "vue"
import { useRoute, useRouter } from "vue-router"

import CategoryOverview from "../components/category/CategoryOverview.vue"
import CategoryDetails from "../components/category/CategoryDetails.vue"
import CategoryDetailPage from "./CategoryDetailPage.vue"

const route = useRoute()
const router = useRouter()

const activeTab = computed(() => route.query.tab || "overview")
const activeCategory = computed(() => route.query.category || null)

const changeTab = (tab) => {
  router.replace({
    path: "/dashboard/category-breakdown",
    query: { tab }
  })
}
</script>

<template>
  <div class="w-full px-6 py-6 text-slate-200 bg-transparent">

    <!-- HEADER -->
    <div class="mb-6">
      <h1 class="text-2xl font-semibold text-white">
        Category Breakdown
      </h1>
      <p class="text-sm text-slate-400 mt-1">
        See how your money is distributed across different categories
      </p>
    </div>

    <!-- TAB SWITCH (hide when inside category) -->
    <div v-if="!activeCategory" class="mb-8">
      <div
        class="inline-flex rounded-xl bg-slate-800/70 p-1 w-[280px]
               border border-white/10"
      >
        <button
          class="flex-1 py-2 text-sm font-medium rounded-lg transition"
          :class="
            activeTab === 'overview'
              ? 'bg-indigo-500/20 text-indigo-400'
              : 'text-slate-400 hover:text-white'
          "
          @click="changeTab('overview')"
        >
          Overview
        </button>

        <button
          class="flex-1 py-2 text-sm font-medium rounded-lg transition"
          :class="
            activeTab === 'details'
              ? 'bg-indigo-500/20 text-indigo-400'
              : 'text-slate-400 hover:text-white'
          "
          @click="changeTab('details')"
        >
          Details
        </button>
      </div>
    </div>

    <!-- CONTENT -->
    <div class="mt-6">

      <!-- OVERVIEW -->
      <CategoryOverview
        v-if="activeTab === 'overview'"
      />

      <!-- CATEGORY LIST -->
      <CategoryDetails
        v-else-if="activeTab === 'details' && !activeCategory"
      />

      <!-- CATEGORY DETAIL PAGE -->
      <CategoryDetailPage
        v-else-if="activeCategory"
      />

    </div>

  </div>
</template>
