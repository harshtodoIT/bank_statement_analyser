<template>
  <div class="min-h-screen bg-gray-50 flex justify-center py-6 px-3 sm:px-6">
    <div class="w-full max-w-5xl">

      <!-- Header -->
      <div class="text-center mb-10 px-3">
        <div class="flex justify-center mb-4">
          <div class="bg-blue-100 p-3 rounded-full">
            <svg
              class="h-6 w-6 text-blue-600"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              stroke-width="3"
            >
              <rect x="5" y="11" width="14" height="10" rx="2" />
              <path d="M8 11V7a4 4 0 018 0v4" />
            </svg>
          </div>
        </div>
        <h1 class="text-2xl sm:text-3xl font-semibold tracking-tight">
          Privacy & Disclosure
        </h1>
        <p class="text-gray-500 mt-2 text-sm sm:text-base max-w-2xl mx-auto">
          Review how your data is handled, stored, and protected. Choose your preferred
          privacy option before continuing.
        </p>
      </div>
      <!-- Data Storage Preference -->
      <div class="bg-white border rounded-xl p-6 mb-6">
        <h2 class="text-lg font-semibold mb-1">Data Storage Preference</h2>
        <p class="text-gray-500 mb-4">
          Choose how you want your uploaded bank statements to be handled.
        </p>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 sm:gap-5">
          <!-- Save -->
          <label
            class="border rounded-xl p-4 sm:p-5 cursor-pointer hover:shadow-md transition-all duration-200"
            :class="storageChoice === 'save'
              ? 'border-blue-500 bg-blue-50 ring-1 ring-blue-300'
              : 'border-gray-200 hover:border-gray-300'"
          >
            <div class="flex items-start gap-3">
              <input
                type="radio"
                class="mt-1 accent-blue-500"
                value="save"
                v-model="storageChoice"
                aria-label="Allow saving data in memory"
              />
              <div>
                <p class="font-medium">Allow saving data in memory</p>
                <p class="text-sm text-gray-500">
                  Your uploaded data will be securely stored in memory and remain available
                  even after refresh or exit for faster access.
                </p>
                <p class="text-xs text-gray-400 mt-1">
                  Best for repeated analysis and reporting.
                </p>
              </div>
            </div>
          </label>
          <!-- No Save -->
          <label
            class="border rounded-xl p-4 sm:p-5 cursor-pointer hover:shadow-md transition-all duration-200"
            :class="storageChoice === 'nosave'
              ? 'border-blue-500 bg-blue-50 ring-1 ring-blue-300'
              : 'border-gray-200 hover:border-gray-300'"
          >
            <div class="flex items-start gap-3">
              <input
                type="radio"
                class="mt-1 accent-blue-500"
                value="nosave"
                v-model="storageChoice"
                aria-label="Do not save data"
              />
              <div>
                <div class="flex items-center gap-2 flex-wrap">
                  <p class="font-medium">Do not save data</p>
                  <span class="text-xs bg-blue-100 text-blue-600 px-2 py-0.5 rounded">
                    Recommended for privacy
                  </span>
                </div>
                <p class="text-sm text-gray-500">
                  Your data will be processed only for this session and permanently deleted
                  when you refresh or close the website.
                </p>
                <p class="text-xs text-gray-400 mt-1">
                  Best for one-time secure analysis.
                </p>
              </div>
            </div>
          </label>
        </div>
        <!-- Dynamic message -->
        <div class="mt-4 bg-blue-50 border border-blue-200 rounded-lg p-3 sm:p-4 text-blue-600 text-sm sm:text-base">
          {{ storageMessage }}
        </div>
      </div>
      <!-- Default Info -->
      <div class="bg-blue-50 border border-blue-200 rounded-lg p-3 sm:p-4 text-blue-600 text-sm sm:text-base mb-6">
        By default, your data is processed only in memory and discarded after session end.
      </div>
      <!-- Trust & Security Banner -->
      <div class="bg-white border rounded-xl p-5 mb-6">
        <div class="flex items-start gap-3">
          <svg class="w-6 h-6 text-green-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path d="M12 3l7 4v5c0 5-3.5 9-7 9s-7-4-7-9V7l7-4z" />
          </svg>
          <div>
            <p class="font-medium">Your data is protected</p>
            <p class="text-sm text-gray-500">
              All uploads are encrypted during processing. We never share your financial
              information with third parties.
            </p>
          </div>
        </div>
      </div>
      <!-- Info Cards -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 sm:gap-5 mb-6">
        <InfoCard title="Data Usage">
          <template #icon>
            <svg class="w-6 h-6 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <ellipse cx="12" cy="5" rx="9" ry="3" />
              <path d="M3 5v14c0 1.7 4 3 9 3s9-1.3 9-3V5" />
            </svg>
          </template>
          Your financial data is used solely for analysis and processing within this application.
          We do not share, sell, or transmit your data to third parties.
        </InfoCard>
        <InfoCard title="AI Limitations">
          <template #icon>
            <svg class="w-6 h-6 text-purple-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path d="M12 2a4 4 0 014 4v2h2a4 4 0 010 8h-2v2a4 4 0 01-8 0v-2H6a4 4 0 010-8h2V6a4 4 0 014-4z"/>
            </svg>
          </template>
          This system uses AI algorithms which may produce errors or inaccuracies.
          Always verify critical information and consult with qualified professionals.
        </InfoCard>
        <InfoCard title="No Financial Advice">
          <template #icon>
            <svg class="w-6 h-6 text-yellow-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path d="M12 9v4m0 4h.01M12 2a10 10 0 100 20 10 10 0 000-20z"/>
            </svg>
          </template>
          This application does not provide financial, investment, or legal advice.
          All outputs are for informational purposes only.
        </InfoCard>
        <InfoCard title="User Responsibility">
          <template #icon>
            <svg class="w-6 h-6 text-green-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path d="M5.1 17a7 7 0 0113.8 0M12 12a4 4 0 100-8 4 4 0 000 8z"/>
            </svg>
          </template>
          You are responsible for the accuracy of uploaded data and how you use the application's
          outputs. Use this tool at your own discretion.
        </InfoCard>
      </div>
      <!-- Consent -->
      <div class="bg-white border rounded-xl p-4 sm:p-5 mb-6">
        <label class="flex items-start gap-3">
          <input
              type="checkbox"
              v-model="accepted"
              class="accent-blue-500 mt-1"
            />

          <span class="text-sm sm:text-base">
            I have read and understood the privacy and disclosure information.
          </span>
        </label>
      </div>
      <!-- Help Banner -->
      <div class="bg-gray-100 border border-gray-200 rounded-xl p-4 mb-6 text-sm text-gray-600">
        Need help understanding these options? Contact your bank administrator or support team
        before continuing.
      </div>
      <!-- Footer -->
      <div class="flex flex-col sm:flex-row gap-3 sm:gap-0 sm:justify-between">
        <button
        class="border rounded px-6 py-2 w-full sm:w-auto"
        @click="router.back()"
      >
        Back
      </button>

      <button
          class="px-6 py-2 rounded text-white w-full sm:w-auto transition"
          :class="canContinue
            ? 'bg-blue-500 hover:bg-blue-600'
            : 'bg-blue-300 cursor-not-allowed'"
          :disabled="!canContinue"
          @click="handleContinue"
        >
          Continue
        </button>


      </div>
    </div>
  </div>
</template>
<script setup>
import { ref, computed } from "vue"
import { useRouter } from "vue-router"
import InfoCard from "../components/icon/InfoCard.vue"

const router = useRouter()

// IMPORTANT: real null
const storageChoice = ref(null)

// Checkbox is optional now
const accepted = ref(false)

const canContinue = computed(() => {
  return storageChoice.value !== null
})

const storageMessage = computed(() => {
  if (storageChoice.value === "save") {
    return "Your data will be securely stored in memory and available for future sessions."
  }
  if (storageChoice.value === "nosave") {
    return "Your data will be processed securely and deleted automatically after this session."
  }
  return "Please select a data storage preference to continue."
})

const handleContinue = () => {
  localStorage.setItem("privacyAccepted", "true")
  localStorage.setItem("storagePreference", storageChoice.value)
  router.push("/upload")
}
</script>

