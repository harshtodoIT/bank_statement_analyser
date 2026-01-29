import api from "./apiClient"

/**
 * Fetch processing history for logged-in user
 * Returns only SUCCESS runs
 */
export async function getProcessingHistory() {
  const response = await api.get("/process/history/")
  return response.data
}
