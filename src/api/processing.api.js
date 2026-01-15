import api from "./apiClient";

/**
 * Start processing job
 * @param {string} fileHash
 * @param {string} sessionId
 */
export async function startProcessing(fileHash, sessionId) {
  const formData = new FormData();
  formData.append("file_hash", fileHash);
  formData.append("session_id", sessionId);

  const response = await api.post(
    "/process/start/",
    formData
  );

  return response.data;
}

export async function getProcessingStatus(jobId) {
  const response = await api.get(
    `/process/status/${jobId}/`
  );

  return response.data;
}
