import { defineStore } from "pinia";
import { uploadStatement } from "../api/upload.api";

export const useUploadStore = defineStore("upload", {
  state: () => ({
    fileHash: null,
    bankName: null,
    sessionId: null,
    loading: false,
    error: null
  }),

  actions: {
    async uploadFile(file) {
      this.loading = true;
      this.error = null;

      try {
        const data = await uploadStatement(file);

        this.fileHash = data.file_hash;
        this.bankName = data.bank_name;
        this.sessionId = data.session_id;

        return true;
      } catch (err) {
        this.error =
          err.response?.data?.error || "Upload failed";
        return false;
      } finally {
        this.loading = false;
      }
    },

    reset() {
      this.fileHash = null;
      this.bankName = null;
      this.sessionId = null;
      this.error = null;
      this.loading = false;
    }
  }
});
