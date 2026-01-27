<script setup>
  // import DashboardHeader from '../components/dashboard/DashboardHeader.vue'
  import KpiCards from '../components/dashboard/KpiCards.vue'
  import HighLevelSummary from '../components/dashboard/HighLevelSummary.vue'
  import IncomeExpenseChart from '../components/dashboard/IncomeExpenseChart.vue';
  // import ExportReport from '../components/dashboard/ExportReport.vue';

  import { onMounted } from "vue";
  import { useDashboardStore } from "../stores/dashboard.store";

  const dashboardStore = useDashboardStore();

  onMounted(() => {
    dashboardStore.fetchDashboardData();
  });

</script>

  <template>
    <div class="space-y-8">

      <!-- KPI Cards -->
      <section>
        <KpiCards />
      </section>

      <!-- Summary + Chart -->
      <section class="grid grid-cols-1 md:grid-cols-2 gap-5 lg:gap-6">
        <HighLevelSummary />
        <IncomeExpenseChart />
      </section>



      <!-- Privacy Notice -->
      <div
        class="mt-6 flex items-start gap-3
               bg-blue-50 border border-blue-200
               text-blue-800
               rounded-xl p-4 text-sm"
      >
        <p>
          <strong>Privacy Notice:</strong>
          By default, your data is processed in memory and discarded.
          No information is stored permanently unless you create an account.
        </p>
      </div>

    </div>
  </template>
