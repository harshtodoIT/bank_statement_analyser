import api from "./apiClient";

export async function getDashboardResults(jobId) {
  const response = await api.get(`/summary/${jobId}/`);
  return response.data;
}
