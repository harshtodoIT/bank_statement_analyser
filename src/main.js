import { createApp } from "vue"
import { createPinia } from "pinia"
import App from "./App.vue"
import { clerkPlugin } from "@clerk/vue"
import router from "./router"

// ✅ IMPORTANT: load Tailwind
import "./assets/styles/main.css"

const app = createApp(App)

const publishableKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

if (!publishableKey) {
  throw new Error("Missing Clerk publishable key")
}

const pinia = createPinia()
app.use(pinia)
app.use(router)

app.use(clerkPlugin, {
  publishableKey,
})

app.mount("#app")
