import { defineStore } from "pinia";
import {
  startProcessing,
  getProcessingStatus
} from "../api/processing.api";
import { useUploadStore } from "./upload.store";

export const useProcessingStore = defineStore("processing", {
  state: () => ({
    jobId: null,
    status: null,
    error: null
  }),

  actions: {
    async startJob() {
      const uploadStore = useUploadStore();

      if (!uploadStore.fileHash || !uploadStore.sessionId) {
        throw new Error("Upload session missing");
      }

      const data = await startProcessing(
        uploadStore.fileHash,
        uploadStore.sessionId
      );

      this.jobId = data.job_id;
      this.status = data.status;
    },

    async pollStatus() {
      if (!this.jobId) return;

      const data = await getProcessingStatus(this.jobId);
      this.status = data.status;

      if (data.status === "FAILED") {
        this.error = data.error;
      }
    },

    reset() {
      this.jobId = null;
      this.status = null;
      this.error = null;
    }
  }
});
