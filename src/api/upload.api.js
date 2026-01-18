import api from "./apiClient";

export async function uploadStatement(file) {
  const formData = new FormData();
  formData.append("file", file);

  const response = await api.post(
    "/uploads/statement/",
    formData
  );

  return response.data;
}
