import { defineStore } from "pinia";
import { uploadStatement } from "../api/upload.api"


export const useUploadStore = defineStore("upload", {
  state: () => ({
    sessionId: null,
    fileHash: null,
    bankName: null,
    loading: false,
    error: null
  }),

  actions: {
    async uploadFile(file) {
      this.loading = true;
      this.error = null;

      try {
        const data = await uploadStatement(file);

        this.sessionId = data.session_id;
        this.fileHash = data.file_hash;
        this.bankName = data.bank_name;

        return true;
      } catch (err) {
        this.error =
          err.response?.data?.error ||
          "Upload failed";

        return false;
      } finally {
        this.loading = false;
      }
    },

    reset() {
      this.$reset();
    }
  }
});
