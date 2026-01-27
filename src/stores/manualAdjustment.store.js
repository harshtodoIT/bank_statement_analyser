import { defineStore } from "pinia";
import { useProcessingStore } from "./processing.store";
import {
  fetchManualAdjustments,
  addManualAdjustment
} from "../api/adjustments.api";

export const useManualAdjustmentStore = defineStore("manualAdjustments", {
  state: () => ({
    loading: false,
    error: null,
    entries: []
  }),

  actions: {
    async loadAdjustments() {
      const processingStore = useProcessingStore();
      if (!processingStore.jobId) return;

      this.loading = true;
      try {
        const res = await fetchManualAdjustments(processingStore.jobId);
        this.entries = res.data || [];
      } catch {
        this.error = "Failed to load manual adjustments";
      } finally {
        this.loading = false;
      }
    },

    async addAdjustment(payload) {
      const processingStore = useProcessingStore();
      if (!processingStore.jobId) return;

      this.loading = true;
      try {
        await addManualAdjustment(processingStore.jobId, payload);
        await this.loadAdjustments();
      } catch {
        this.error = "Failed to add manual adjustment";
      } finally {
        this.loading = false;
      }
    }
  }
});
