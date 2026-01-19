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

    // 🎨 Create gradients (subtle, fintech style)
    const incomeGradient = ctx.createLinearGradient(0, 0, 200, 200)
    incomeGradient.addColorStop(0, '#6366F1') // Indigo
    incomeGradient.addColorStop(1, '#4F46E5')

    const expenseGradient = ctx.createLinearGradient(0, 0, 200, 200)
    expenseGradient.addColorStop(0, '#38BDF8') // Sky
    expenseGradient.addColorStop(1, '#0EA5E9')

    const uncategorizedGradient = ctx.createLinearGradient(0, 0, 200, 200)
    uncategorizedGradient.addColorStop(0, '#CBD5E1') // Slate light
    uncategorizedGradient.addColorStop(1, '#94A3B8')

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
            borderColor: '#ffffff'
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
            backgroundColor: '#111827',
            titleColor: '#ffffff',
            bodyColor: '#e5e7eb',
            padding: 10,
            cornerRadius: 8
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
