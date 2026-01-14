import { createRouter, createWebHistory } from "vue-router"

// Views
// import HomeView from '../views/homeView.vue'
import UploadView from '../views/UploadView.vue'
import ProcessingView from '../views/ProcessingView.vue'
// import ErrorView from '../views/ErrorView.vue'
import DashboardView from '../views/DashboardView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      redirect: "/upload"
    },
    {
      path: "/upload",
      component: UploadView
    },
    {
      path: "/processing",
      component: ProcessingView
    },
    {
      path: "/dashboard",
      component: DashboardView
    }
  ],
})

export default router
