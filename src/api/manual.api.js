import api from "./apiClient"

/**
 * Create a manual adjustment for a processed job
 * @param {string} jobId
 * @param {{ label: string, amount: number, note?: string }} payload
 */
export async function createManualAdjustment(jobId, payload) {
  const res = await api.post(
    `/adjustments/${jobId}/`,
    payload
  )
  return res.data
}
