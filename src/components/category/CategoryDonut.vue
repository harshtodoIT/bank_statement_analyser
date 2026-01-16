<script setup>
  import { onMounted, ref } from 'vue'
  import {
    Chart,
    DoughnutController,
    ArcElement,
    Tooltip,
    Legend
  } from 'chart.js'

  Chart.register(DoughnutController, ArcElement, Tooltip, Legend)

  const canvasRef = ref(null)

  onMounted(() => {
    new Chart(canvasRef.value, {
      type: 'doughnut',
      data: {
        labels: ['Income', 'Expenses', 'Uncategorized'],
        datasets: [
          {
            data: [6650, 4150, 485],
            backgroundColor: ['#22c55e', '#ef4444', '#f97316'],
            hoverOffset: 10,
            borderWidth: 0
          }
        ]
      },
      options: {
        cutout: '70%',
        responsive: true,
        plugins: {
          legend: {
            position: 'bottom',
            labels: {
              usePointStyle: true,
              padding: 20
            }
          },
          tooltip: {
            callbacks: {
              label: (ctx) => {
                const value = ctx.raw
                return `${ctx.label}: ₹${value.toLocaleString()}`
              }
            }
          }
        }
      }
    })
  })
  </script>

  <template>
    <div class="flex justify-center items-center py-10">
      <canvas ref="canvasRef" class="max-w-[320px]" />
    </div>
  </template>
