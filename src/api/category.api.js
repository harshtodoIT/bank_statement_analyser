import api from "./apiClient"

export async function getCategoryDrillDown({ job_id, category }) {
  const response = await api.get("/categorization/drill-down/", {
    params: {
      job_id,
      category,
    },
  })

  return response.data
}
