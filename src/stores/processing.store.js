import { defineStore } from "pinia"
import {
  startProcessing,
  getProcessingStatus
} from "../api/processing.api"
import { useUploadStore } from "./upload.store"

export const useProcessingStore = defineStore("processing", {
  state: () => ({
    jobId: localStorage.getItem("job_id"),
    status: localStorage.getItem("job_status"), // 🔧 restore status
    error: null
  }),

  getters: {
    hasActiveJob: (state) =>
      !!state.jobId && state.status === "SUCCESS"
  },

  actions: {
    async startJob() {
      const uploadStore = useUploadStore()

      if (!uploadStore.fileHash || !uploadStore.sessionId) {
        throw new Error("Upload session missing")
      }

      const data = await startProcessing(
        uploadStore.fileHash,
        uploadStore.sessionId
      )

      this.jobId = data.job_id
      this.status = data.status

      // ✅ persist both
      localStorage.setItem("job_id", data.job_id)
      localStorage.setItem("job_status", data.status)
    },

    async pollStatus() {
      if (!this.jobId) return

      const data = await getProcessingStatus(this.jobId)

      this.status = data.status
      localStorage.setItem("job_status", data.status)

      if (data.status === "FAILED") {
        this.error = data.error
      }
    },

    setJob(jobId) {
      this.jobId = jobId
      this.status = "SUCCESS"

      localStorage.setItem("job_id", jobId)
      localStorage.setItem("job_status", "SUCCESS")
    },

    reset() {
      this.jobId = null
      this.status = null
      this.error = null

      localStorage.removeItem("job_id")
      localStorage.removeItem("job_status")
    }
  }
})
