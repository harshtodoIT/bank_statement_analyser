import axios from "axios"

const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api",
  withCredentials: true,
})

/**
 * 🔐 Attach Clerk JWT automatically
 */
api.interceptors.request.use(async (config) => {
  const clerk = window.Clerk

  if (clerk && clerk.session) {
    const token = await clerk.session.getToken({
      template: "backend",
    })

    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
  }

  return config
})

export default api
