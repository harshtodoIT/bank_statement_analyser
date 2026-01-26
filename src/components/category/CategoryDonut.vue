<script setup>
  import { onMounted, ref, onBeforeUnmount } from 'vue'
  import {
    Chart,
    PieController,
    ArcElement,
    Tooltip
  } from 'chart.js'

  Chart.register(PieController, ArcElement, Tooltip)

  const chartRef = ref(null)
  let chartInstance = null

  const values = {
    income: 6650,
    expenses: 4150,
    uncategorized: 300
  }

  onMounted(() => {
    const ctx = chartRef.value.getContext('2d')

      // 🎨 Create gradients (dark UI optimized)
const incomeGradient = ctx.createLinearGradient(0, 0, 200, 200)
incomeGradient.addColorStop(0, '#818CF8') // indigo-400
incomeGradient.addColorStop(1, '#4F46E5') // indigo-600

const expenseGradient = ctx.createLinearGradient(0, 0, 200, 200)
expenseGradient.addColorStop(0, '#7DD3FC') // sky-300
expenseGradient.addColorStop(1, '#0284C7') // sky-600

const uncategorizedGradient = ctx.createLinearGradient(0, 0, 200, 200)
uncategorizedGradient.addColorStop(0, '#64748B') // slate-500
uncategorizedGradient.addColorStop(1, '#475569') // slate-600


    chartInstance = new Chart(ctx, {
      type: 'pie',
      data: {
        labels: ['Income', 'Expenses', 'Uncategorized'],
        datasets: [
          {
            data: [
              values.income,
              values.expenses,
              values.uncategorized
            ],
            backgroundColor: [
              incomeGradient,
              expenseGradient,
              uncategorizedGradient
            ],
            borderWidth: 2,
            borderColor: '#0F172A'
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
            backgroundColor: '#020617', // slate-950
            titleColor: '#ffffff',
            bodyColor: '#CBD5E1', // slate-300
            padding: 12,
            cornerRadius: 10,
            boxPadding: 6
          }

        }
      }
    })
  })

  onBeforeUnmount(() => {
    if (chartInstance) chartInstance.destroy()
  })
  </script>

  <template>
    <!-- Slightly reduced size for balance -->
    <div class="w-[220px] h-[220px] mx-auto">
      <canvas ref="chartRef"></canvas>
    </div>
  </template>
