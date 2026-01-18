<script setup>
  import { ref } from 'vue'
  import CategoryOverview from '../components/category/CategoryOverview.vue'
  import CategoryDetails from '../components/category/CategoryDetails.vue'


  /**
   * UI STATE
   * overview | details
   */
  const activeTab = ref('overview')
  </script>


  <template>
    <div class="w-full px-6 py-6">
      <!-- ================= HEADER ================= -->
      <div class="mb-6">
        <h1 class="text-2xl font-semibold text-gray-900">
          Category Breakdown
        </h1>
        <p class="text-sm text-gray-500 mt-1">
          See how your money is distributed across different categories
        </p>
      </div>

      <!-- ================= TAB SWITCH ================= -->
      <div class="mb-8">
        <div
          class="inline-flex rounded-full bg-gray-100 p-1 w-[280px]"
        >
          <button
            class="flex-1 py-2 text-sm font-medium rounded-full transition"
            :class="
              activeTab === 'overview'
                ? 'bg-white text-gray-900 shadow'
                : 'text-gray-500'
            "
            @click="activeTab = 'overview'"
          >
            Overview
          </button>

          <button
            class="flex-1 py-2 text-sm font-medium rounded-full transition"
            :class="
              activeTab === 'details'
                ? 'bg-white text-gray-900 shadow'
                : 'text-gray-500'
            "
            @click="activeTab = 'details'"
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
