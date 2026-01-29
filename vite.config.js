import { defineConfig } from "vite"
import vue from "@vitejs/plugin-vue"
import tailwindcss from "@tailwindcss/vite"

export default defineConfig({
  plugins: [
    vue(),
    tailwindcss(),
  ],

  server: {
    proxy: {
      // Uploads
      "/uploads": {
        target: "http://localhost:8000",
        changeOrigin: true,
      },

      // Processing
      "/process": {
        target: "http://localhost:8000",
        changeOrigin: true,
      },

      // Results / dashboard data
      "/results": {
        target: "http://localhost:8000",
        changeOrigin: true,
      },

      // Reporting / exports if used
      "/report": {
        target: "http://localhost:8000",
        changeOrigin: true,
      },

      // Privacy / statements / categorization
      "/privacy": {
        target: "http://localhost:8000",
        changeOrigin: true,
      },
      "/statements": {
        target: "http://localhost:8000",
        changeOrigin: true,
      },
      "/categorization": {
        target: "http://localhost:8000",
        changeOrigin: true,
      },
    },
  },
})
