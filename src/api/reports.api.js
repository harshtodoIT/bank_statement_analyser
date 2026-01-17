import api from "./apiClient";

export const downloadCSV = (jobId) => {
  return api.get(`/export/csv/${jobId}/`, {
    responseType: "blob"
  });
};

export const downloadPDF = (jobId) => {
  return api.get(`/export/pdf/${jobId}/`, {
    responseType: "blob"
  });
};
