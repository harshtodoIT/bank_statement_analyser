import { createApp } from "vue"
import { createPinia } from "pinia"
import App from "./App.vue"
import router from "./router"
import { clerkPlugin } from "@clerk/vue"

// styles
import "./assets/styles/main.css"

const publishableKey = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY

if (!publishableKey) {
  throw new Error("Missing Clerk publishable key")
}

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.use(clerkPlugin, {
  publishableKey,
})

app.mount("#app")
