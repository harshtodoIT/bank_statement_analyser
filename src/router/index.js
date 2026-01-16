import { createRouter, createWebHistory } from "vue-router"

import HomeView from '../views/homeView.vue'
import UploadView from '../views/UploadView.vue'
import ProcessingView from '../views/ProcessingView.vue'
import ErrorView from '../views/ErrorView.vue'
import DashboardView from '../views/DashboardView.vue'
import DashboardLayout from '../layouts/DashboardLayout.vue'
import CategoryBreakdownView from '../views/CategoryBreakdownView.vue'
import MonthlySummaryView from '../views/MonthlySummaryView.vue'
import ReportsView from '../views/ReportsView.vue'




const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeView,
    },
    {
      path: '/upload',
      name: 'Upload',
      component: UploadView,
    },
    {
      path: '/processing',
      name: 'Processing',
      component: ProcessingView,
    },
    {
      path: '/dashboard',
      component: DashboardLayout,
      children: [
        {
          path: '',
          name: 'dashboard',
          component: DashboardView
        },
        {
          path: 'category-breakdown',
          name: 'category-breakdown',
          component: CategoryBreakdownView
        },
        {
          path: 'monthly-summary',
          name: 'monthly-summary',
          component: MonthlySummaryView
        },
        {
          path: 'reports',
          name: 'reports',
          component: ReportsView
        },
        {
          path: 'manual-adjustment',
          name: 'manual-adjustment',
          component: () => import('../views/ManualAdjustmentView.vue')

        }

      ]
    },
    {
      path: '/error',
      name: 'Error',
      component: ErrorView,
    },

  ],
})

export default router
