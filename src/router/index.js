import { createRouter, createWebHistory } from "vue-router"

import LoginView from "../views/LoginView.vue"
import UploadView from "../views/UploadView.vue"
import ProcessingView from "../views/ProcessingView.vue"
import PrivacyDisclosure from "../views/PrivacyDisclosure.vue"

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
    { path: "/", redirect: "/login" },

    { path: "/login", component: LoginView },
    { path: "/privacy", component: PrivacyDisclosure },
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
  ],
})

router.beforeEach(async (to) => {
  const clerk = window.Clerk
  if (!clerk) return true

  await clerk.load()

  const isSignedIn = !!clerk.user?.id

  // 🔒 NOT SIGNED IN
  if (!isSignedIn) {
    if (to.path !== "/login") return "/login"
    return true
  }

  // ✅ SIGNED IN — get token properly
  const token = await clerk.session?.getToken()
  if (!token) return "/login"

  try {
    const response = await fetch("http://127.0.0.1:8000/api/privacy/status/", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })

    if (!response.ok) {
      console.error("Failed privacy check")
      return "/login"
    }

    const data = await response.json()
    const privacyAccepted = data.has_chosen
    
    // 🚨 If NOT accepted → force privacy page
    if (!privacyAccepted && to.path !== "/privacy") {
      return "/privacy"
    }

    // ✅ If accepted and user on login → go dashboard
    if (privacyAccepted && to.path === "/login") {
      return "/dashboard"
    }

  } catch (error) {
    console.error("Privacy check error:", error)
    return "/login"
  }

  return true
})

export default router
