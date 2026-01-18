<script setup>
  import { onMounted, ref, watch } from "vue";
  import { useDashboardStore } from "../../stores/dashboard.store";
  import {
    Chart,
    DoughnutController,
    ArcElement,
    Tooltip,
    Legend
  } from "chart.js";

  Chart.register(DoughnutController, ArcElement, Tooltip, Legend);

  const store = useDashboardStore();
  const canvasRef = ref(null);
  let chart = null;

  function renderChart() {
    if (!canvasRef.value) return;

    const income = store.totals.income || 0;
    const expense = store.totals.expense || 0;
    const uncategorized = store.uncategorizedAmount || 0;

    // ⛔ Do not render empty chart
    if (income === 0 && expense === 0 && uncategorized === 0) return;

    if (chart) {
      chart.data.datasets[0].data = [
        income,
        expense,
        uncategorized
      ];
      chart.update();
      return;
    }

    chart = new Chart(canvasRef.value, {
      type: "doughnut",
      data: {
        labels: ["Income", "Expenses", "Uncategorized"],
        datasets: [
          {
            data: [income, expense, uncategorized],
            backgroundColor: ["#22C55E", "#EF4444", "#F97316"],
            hoverOffset: 10,
            borderWidth: 0
          }
        ]
      },
      options: {
        cutout: "70%",
        responsive: true,
        plugins: {
          legend: {
            position: "bottom",
            labels: {
              usePointStyle: true,
              padding: 20
            }
          },
          tooltip: {
            callbacks: {
              label: (ctx) =>
                `${ctx.label}: ₹${ctx.raw.toLocaleString()}`
            }
          }
        }
      }
    });
  }

  onMounted(renderChart);

  // ✅ Watch the actual reactive sources
  watch(
    () => [
      store.totals.income,
      store.totals.expense,
      store.uncategorizedAmount
    ],
    renderChart
  );
  </script>

  <template>
    <div class="flex justify-center items-center py-10">
      <canvas ref="canvasRef" class="max-w-[320px]" />
    </div>
  </template>
