import axios from "axios"

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  withCredentials: true,
})

// 🔐 HARD BLOCK REQUESTS UNTIL CLERK IS READY
api.interceptors.request.use(async (config) => {
  // Wait until Clerk is injected
  while (!window.Clerk) {
    await new Promise(resolve => setTimeout(resolve, 10))
  }

  const clerk = window.Clerk

  // Wait until Clerk is fully loaded
  if (!clerk.loaded) {
    await clerk.load()
  }

  // Attach token if session exists
  if (clerk.session) {
    const token = await clerk.session.getToken()
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
  }

  return config
})

export default api
