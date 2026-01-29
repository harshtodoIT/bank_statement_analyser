import { defineStore } from "pinia"
import { getPrivacyStatus } from "../api/privacy.api"

export const usePrivacyStore = defineStore("privacy", {
  state: () => ({
    loaded: false,
    hasChosen: false,
    privacyMode: null, // "TEMPORARY" | "PERSIST"
    error: null
  }),

  getters: {
    isTemporary: (state) => state.privacyMode === "TEMPORARY",
    isPersist: (state) => state.privacyMode === "PERSIST"
  },

  actions: {
    async fetchStatus() {
      if (this.loaded) return

      try {
        const res = await getPrivacyStatus()
        const data = res.data ?? res

        this.hasChosen = !!data.has_chosen
        this.privacyMode = data.privacy_mode
        this.loaded = true
      } catch (err) {
        console.error("Privacy status fetch failed", err)
        this.error = "Failed to load privacy status"
        this.loaded = true
      }
    },

    reset() {
      this.loaded = false
      this.hasChosen = false
      this.privacyMode = null
      this.error = null
    }
  }
})
