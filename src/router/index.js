import { createRouter, createWebHistory } from "vue-router"

// import HomeView from '../views/homeView.vue'
import CategoryDetailPage from '../views/CategoryDetailPage.vue'
import PrivacyDisclosure from '../views/PrivacyDisclosure.vue'
import UploadView from '../views/UploadView.vue'
import ProcessingView from '../views/ProcessingView.vue'
import ErrorView from '../views/ErrorView.vue'
import DashboardView from '../views/DashboardView.vue'
import DashboardLayout from '../layouts/DashboardLayout.vue'
import CategoryBreakdownView from '../views/CategoryBreakdownView.vue'
import MonthlySummaryView from '../views/MonthlySummaryView.vue'
import ReportsView from '../views/ReportsView.vue'
import ManualAdjustmentView from "../views/ManualAdjustmentView.vue"




const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/privacy',
      name: 'PrivacyDisclosure',
      component: PrivacyDisclosure,
    },
    {
      path: '/',
      redirect: '/upload'
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
          component: DashboardView,
          meta: { title: 'Dashboard' }
        },
        {
          path: 'category-breakdown',
          component: CategoryBreakdownView,
          // meta: { title: 'Category Breakdown' }
        },
        {
          path: 'category/:category',
          name: 'CategoryDetail',
          component: CategoryDetailPage,
          meta: { title: 'Category Details' }
        },
        {
          path: 'monthly-summary',
          component: MonthlySummaryView,
          meta: { title: 'Monthly Summary' }
        },
        {
          path: 'reports',
          component: ReportsView,
          meta: { title: 'Reports' }
        },
        {
          path: 'manual-adjustment',
          component: ManualAdjustmentView,
          meta: { title: 'Manual Adjustment' }
        },
        {
          path: 'history',
          component: () => import('../views/HistoryView.vue')
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

router.beforeEach((to, from, next) => {
  const privacyAccepted = localStorage.getItem("privacyAccepted")

  // If user tries to go to upload without accepting privacy
  if (to.path === "/upload" && !privacyAccepted) {
    next("/privacy") // force privacy page
  } else {
    next() // allow navigation
  }
})


export default router
