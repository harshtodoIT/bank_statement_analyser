import { createRouter, createWebHistory } from "vue-router"

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "upload",
      component: () => import("../views/UploadView.vue"),
    },
    {
      path: "/processing",
      name: "processing",
      component: () => import("../views/ProcessingView.vue"),
    },
    {
      path: "/error",
      name: "error",
      component: () => import("../views/ErrorView.vue"),
    },
  ],
})

export default router
