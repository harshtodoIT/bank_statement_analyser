import { createRouter, createWebHistory } from "vue-router"

import UploadView from "../views/UploadView.vue"
import ProcessingView from "../views/ProcessingView.vue"
import ErrorView from "../views/ErrorView.vue"
import DashboardView from "../views/DashboardView.vue"
import DashboardLayout from "../layouts/DashboardLayout.vue"
import CategoryBreakdownView from "../views/CategoryBreakdownView.vue"
import MonthlySummaryView from "../views/MonthlySummaryView.vue"
import ReportsView from "../views/ReportsView.vue"
import HomeView from "../views/homeView.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "Home",
      component: HomeView,
      meta: { public: true },
    },

    {
      path: "/upload",
      name: "Upload",
      component: UploadView,
      meta: { requiresAuth: true },
    },

    {
      path: "/processing",
      name: "Processing",
      component: ProcessingView,
      meta: { requiresAuth: true },
    },

    {
      path: "/dashboard",
      component: DashboardLayout,
      meta: { requiresAuth: true },
      children: [
        {
          path: "",
          name: "dashboard",
          component: DashboardView,
        },
        {
          path: "category-breakdown",
          component: CategoryBreakdownView,
        },
        {
          path: "monthly-summary",
          component: MonthlySummaryView,
        },
        {
          path: "reports",
          component: ReportsView,
        },
        {
          path: "manual-adjustment",
          component: () =>
            import("../views/ManualAdjustmentView.vue"),
        },
      ],
    },

    {
      path: "/error",
      component: ErrorView,
    },

    {
      path: "/:pathMatch(.*)*",
      redirect: "/",
    },
  ],
})

/**
 * 🔐 GLOBAL AUTH GUARD (CLERK SAFE)
 */
router.beforeEach(async (to) => {
  const clerk = window.Clerk

  if (!clerk) return true

  await clerk.load()

  const isSignedIn = !!clerk.user

  if (to.meta.requiresAuth && !isSignedIn) {
    return "/"
  }

  if (to.meta.public && isSignedIn && to.path === "/") {
    return "/upload"
  }

  return true
})

export default router
