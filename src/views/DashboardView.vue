<script setup>
  import DashboardHeader from '../components/dashboard/DashboardHeader.vue'
  import KpiCards from '../components/dashboard/KpiCards.vue'
  import HighLevelSummary from '../components/dashboard/HighLevelSummary.vue'
  import IncomeExpenseChart from '../components/dashboard/IncomeExpenseChart.vue';
  import ExportReport from '../components/dashboard/ExportReport.vue';

  import { onMounted } from "vue";
  import { useDashboardStore } from "../stores/dashboard.store";

  const dashboardStore = useDashboardStore();

  onMounted(() => {
    dashboardStore.fetchDashboardData();
  });

</script>

  <template>
    <div class="space-y-8">

      <!-- Dashboard Header -->
      <section>
        <DashboardHeader />
      </section>

      <!-- KPI Cards -->
      <section>
        <KpiCards />
      </section>

      <!-- High Level Summary + Chart -->
      <section class="grid grid-cols-1 lg:grid-cols-2 gap-6">
  <div>
    <HighLevelSummary />
  </div>

  <div>
    <IncomeExpenseChart/>
  </div>
</section>

      <!-- Actions -->
      <section class="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-8">
        <ExportReport class="col-span-2" />
      </section>


    </div>
    <div
  class="mt-6 flex items-start gap-3
         bg-blue-50 border border-blue-200
         text-blue-800
         rounded-xl p-4 text-sm"
>
  <svg
    class="w-5 h-5 mt-0.5"
    fill="none"
    stroke="currentColor"
    stroke-width="2"
    viewBox="0 0 24 24"
  >
    <path
      stroke-linecap="round"
      stroke-linejoin="round"
      d="M13 16h-1v-4h-1m1-4h.01M12 18a6 6 0 100-12 6 6 0 000 12z"
    />
  </svg>

  <p>
    <strong>Privacy Notice:</strong>
    By default, your data is processed in memory and discarded.
    No information is stored permanently unless you create an account.
  </p>
</div>

  </template>
