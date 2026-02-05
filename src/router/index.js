import { createRouter, createWebHistory } from "vue-router"
import { useProcessingStore } from "../stores/processing.store"

import LoginView from "../views/LoginView.vue"
import UploadView from "../views/UploadView.vue"
import ProcessingView from "../views/ProcessingView.vue"

import DashboardLayout from "../layouts/DashboardLayout.vue"
import DashboardView from "../views/DashboardView.vue"
import CategoryBreakdownView from "../views/CategoryBreakdownView.vue"
import CategoryDetailPage from "../views/CategoryDetailPage.vue"
import MonthlySummaryView from "../views/MonthlySummaryView.vue"
import ManualAdjustmentView from "../views/ManualAdjustmentView.vue"
import HistoryView from "../views/HistoryView.vue"

import ErrorView from "../views/ErrorView.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: "/", redirect: "/upload" },

    { path: "/login", component: LoginView },

    { path: "/upload", component: UploadView },
    { path: "/processing", component: ProcessingView },

    {
      path: "/dashboard",
      component: DashboardLayout,
      children: [
        { path: "", component: DashboardView },
        { path: "category-breakdown", component: CategoryBreakdownView },
        { path: "category/:category", component: CategoryDetailPage },
        { path: "monthly-summary", component: MonthlySummaryView },
        { path: "manual-adjustment", component: ManualAdjustmentView },
        { path: "history", component: HistoryView },
      ],
    },

    { path: "/error", component: ErrorView },
    { path: "/:pathMatch(.*)*", redirect: "/dashboard" },
  ],
})

let lastUserId = null

router.beforeEach(async (to) => {
  const clerk = window.Clerk
  if (!clerk) return true

  await clerk.load()
  const processingStore = useProcessingStore()

  const currentUserId = clerk.user?.id || null

  // 🔥 CRITICAL FIX
  // If auth user changed → reset processing state
  if (lastUserId !== currentUserId) {
    processingStore.reset()
    lastUserId = currentUserId
  }

  const isSignedIn = !!currentUserId

  // 🔒 NOT SIGNED IN
  if (!isSignedIn) {
    return to.path === "/login" ? true : "/login"
  }

  // 🔄 PROCESSING ACTIVE → LOCK EVERYTHING EXCEPT PROCESSING
  if (processingStore.jobId && processingStore.status === "PROCESSING") {
    return to.path === "/processing" ? true : "/processing"
  }

  // 🚫 PROCESSING DONE → BLOCK PROCESSING PAGE
  if (processingStore.status === "SUCCESS" && to.path === "/processing") {
    return "/dashboard"
  }

  return true
})

export default router
