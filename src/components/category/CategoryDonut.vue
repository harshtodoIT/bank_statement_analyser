<script setup>
import { onMounted, ref, watch, onBeforeUnmount } from "vue"
import { useDashboardStore } from "../../stores/dashboard.store"

import {
  Chart,
  PieController,
  ArcElement,
  Tooltip
} from "chart.js"

Chart.register(PieController, ArcElement, Tooltip)

const store = useDashboardStore()
const chartRef = ref(null)
let chartInstance = null

function renderChart() {
  if (!chartRef.value) return

  const income = store.totals.income || 0
  const expenses = store.totals.expense || 0
  const uncategorized = store.uncategorizedAmount || 0

  // do not render empty chart
  if (income === 0 && expenses === 0 && uncategorized === 0) return

  const ctx = chartRef.value.getContext("2d")

  // gradients (dark UI)
  const incomeGradient = ctx.createLinearGradient(0, 0, 200, 200)
  incomeGradient.addColorStop(0, "#818CF8")
  incomeGradient.addColorStop(1, "#4F46E5")

  const expenseGradient = ctx.createLinearGradient(0, 0, 200, 200)
  expenseGradient.addColorStop(0, "#7DD3FC")
  expenseGradient.addColorStop(1, "#0284C7")

  const uncategorizedGradient = ctx.createLinearGradient(0, 0, 200, 200)
  uncategorizedGradient.addColorStop(0, "#64748B")
  uncategorizedGradient.addColorStop(1, "#475569")

  if (chartInstance) {
    chartInstance.data.datasets[0].data = [
      income,
      expenses,
      uncategorized
    ]
    chartInstance.update()
    return
  }

  chartInstance = new Chart(ctx, {
    type: "pie",
    data: {
      labels: ["Income", "Expenses", "Uncategorized"],
      datasets: [
        {
          data: [income, expenses, uncategorized],
          backgroundColor: [
            incomeGradient,
            expenseGradient,
            uncategorizedGradient
          ],
          borderWidth: 2,
          borderColor: "#0F172A"
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: {
          enabled: true,
          backgroundColor: "#020617",
          titleColor: "#FFFFFF",
          bodyColor: "#CBD5E1",
          padding: 12,
          cornerRadius: 10,
          boxPadding: 6,
          callbacks: {
            label: ctx =>
              `${ctx.label}: ₹${ctx.raw.toLocaleString()}`
          }
        }
      }
    }
  })
}

onMounted(renderChart)

watch(
  () => [
    store.totals.income,
    store.totals.expense,
    store.uncategorizedAmount
  ],
  renderChart
)

onBeforeUnmount(() => {
  if (chartInstance) chartInstance.destroy()
})
</script>

<template>
  <div class="w-[220px] h-[220px] mx-auto">
    <canvas ref="chartRef"></canvas>
  </div>
</template>
