import { createRouter, createWebHistory } from "vue-router"

// Views
import HomeView from '../views/homeView.vue'
import UploadView from '../views/UploadView.vue'
import ProcessingView from '../views/ProcessingView.vue'
import ErrorView from '../views/ErrorView.vue'
import DashboardView from '../views/DashboardView.vue'

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
      name: 'Dashboard',
      component: DashboardView,
    },
    {
      path: '/error',
      name: 'Error',
      component: ErrorView,
    },
  ],
})

export default router
