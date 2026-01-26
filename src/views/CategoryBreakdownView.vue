<script setup>
  import { ref } from 'vue'
  import CategoryOverview from '../components/category/CategoryOverview.vue'
  import CategoryDetails from '../components/category/CategoryDetails.vue'


  /**
   * UI STATE
   * overview | details
   */
   import { useRoute, useRouter } from 'vue-router'

  const route = useRoute()
  const router = useRouter()


  const activeTab = ref(route.query.tab || 'overview')
        const changeTab = (tab) => {
          activeTab.value = tab

          router.replace({
            path: '/dashboard/category-breakdown',
            query: { tab }
          })
        }
        import { watch } from 'vue'

        watch(
          () => route.query.tab,
          (tab) => {
            activeTab.value = tab || 'overview'
          }
        )



  </script>


<template>
  <div class="w-full px-6 py-6 text-slate-200 bg-transparent">

    <!-- ================= HEADER ================= -->
    <div class="mb-6">
      <h1 class="text-2xl font-semibold text-white">
        Category Breakdown
      </h1>
      <p class="text-sm text-slate-400 mt-1">
        See how your money is distributed across different categories
      </p>
    </div>

    <!-- ================= TAB SWITCH ================= -->
    <div class="mb-8">
      <div
        class="inline-flex rounded-xl bg-slate-800/70 p-1 w-[280px]
               border border-white/10"
      >
        <!-- Overview -->
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

        <!-- Details -->
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

    <!-- ================= CONTENT AREA ================= -->
    <div class="mt-6">
      <!-- OVERVIEW TAB -->
      <div v-if="activeTab === 'overview'">
        <CategoryOverview />
      </div>

      <!-- DETAILS TAB -->
      <div v-else>
        <CategoryDetails />
      </div>
    </div>

  </div>
</template>
