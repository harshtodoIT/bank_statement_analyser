import api from "./apiClient"

export async function getPrivacyStatus() {
  const res = await api.get("/privacy/status/")
  return res.data
}
