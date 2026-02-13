<script setup>
import { ref, onMounted, onUnmounted } from "vue"
import { useRouter } from "vue-router"
import { useProcessingStore } from "../stores/processing.store"
import { SignedIn, SignedOut, RedirectToSignIn } from "@clerk/vue"


const router = useRouter()
const processingStore = useProcessingStore()

const progress = ref(10)
const isSuccess = ref(false)
const isCompleted = ref(false) // 🔒 HARD LOCK AFTER SUCCESS

const steps = ref([
  { key: "upload", label: "Uploading file", status: "done" },
  { key: "read", label: "Reading statement", status: "done" },
  { key: "extract", label: "Extracting transactions", status: "loading" },
  { key: "categorize", label: "Categorizing data", status: "pending" },
  { key: "finalize", label: "Finalizing analysis", status: "pending" }
])

let timer = null

onMounted(async () => {
  try {
    // ✅ DO NOT restart job if already exists
    if (!processingStore.jobId) {
      await processingStore.startJob()
    }
  } catch {
    router.replace("/upload")
    return
  }

  timer = setInterval(async () => {
    if (isCompleted.value) return

    await processingStore.pollStatus()

    if (processingStore.status === "PROCESSING") {
      progress.value = Math.min(progress.value + 10, 90)
    }

    if (processingStore.status === "SUCCESS" && !isCompleted.value) {
      isCompleted.value = true
      progress.value = 100
      isSuccess.value = true

      steps.value.forEach(step => {
        step.status = "done"
      })

      clearInterval(timer)

      setTimeout(() => {
        router.replace("/dashboard")
      }, 1500)
    }


    if (processingStore.status === "FAILED") {
      clearInterval(timer)
      console.error(processingStore.error)
      router.replace("/error")
    }
  }, 2000)
})

onUnmounted(() => {
  if (timer) clearInterval(timer)
})
</script>

<template>
  <SignedIn>
  <div
    class="min-h-screen flex items-center justify-center px-4
           bg-gradient-to-br from-[#0b1220] via-[#0e1628] to-[#111827]"
  >
    <div
      class="w-full max-w-2xl rounded-2xl border border-white/10
             bg-slate-900/80 backdrop-blur-xl shadow-2xl p-8
             transition-all duration-500"
      :class="isSuccess && 'ring-2 ring-green-500/40'"
    >

      <!-- TITLE -->
      <div class="text-center mb-8">
        <h1 class="text-2xl font-semibold text-white">
          {{ isSuccess ? "Analysis Complete" : "Processing Your Statement" }}
        </h1>
        <p class="text-slate-400 mt-2 text-sm">
          {{ isSuccess
            ? "Your dashboard is ready."
            : "Securely analysing your bank data. Please don’t refresh." }}
        </p>
      </div>

      <!-- ICON -->
      <div class="flex justify-center mb-6">
        <div
          class="w-16 h-16 rounded-full flex items-center justify-center
                 transition-all duration-500"
          :class="isSuccess
            ? 'bg-green-500/20 scale-110'
            : 'bg-indigo-500/20'"
        >
          <svg
            v-if="isSuccess"
            class="w-8 h-8 text-green-400 animate-pop"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="3"
            stroke-linecap="round"
            stroke-linejoin="round"
          >
            <polyline points="20 6 9 17 4 12" />
          </svg>

          <svg
            v-else
            class="w-6 h-6 text-indigo-400 animate-spin"
            viewBox="0 0 24 24"
          >
            <circle
              class="opacity-20"
              cx="12"
              cy="12"
              r="10"
              stroke="currentColor"
              stroke-width="3"
              fill="none"
            />
            <path
              d="M22 12a10 10 0 01-10 10"
              stroke="currentColor"
              stroke-width="3"
              stroke-linecap="round"
              fill="none"
            />
          </svg>
        </div>
      </div>

      <!-- PROGRESS -->
      <div class="mb-8">
        <div class="flex justify-between text-xs text-slate-400 mb-2">
          <span>Progress</span>
          <span>{{ progress }}%</span>
        </div>

        <div class="w-full h-2 rounded-full bg-white/10 overflow-hidden">
          <div
            class="h-full rounded-full transition-all duration-700"
            :class="isSuccess
              ? 'bg-green-500'
              : 'bg-gradient-to-r from-indigo-500 to-purple-500'"
            :style="{ width: progress + '%' }"
          />
        </div>
      </div>

      <!-- STEPS -->
      <div class="space-y-4">
        <div
          v-for="step in steps"
          :key="step.key"
          class="flex items-center gap-4 p-4 rounded-xl
                 border border-white/10 bg-white/5"
        >
          <div
            class="w-9 h-9 rounded-full flex items-center justify-center"
            :class="step.status === 'done'
              ? 'bg-green-500/20 text-green-400'
              : 'bg-indigo-500/20 text-indigo-400'"
          >
            <span v-if="step.status === 'done'">✔</span>
            <span v-else class="animate-pulse">…</span>
          </div>

          <p class="text-sm text-slate-200">
            {{ step.label }}
          </p>
        </div>
      </div>

      <!-- FOOTER -->
      <p class="mt-8 text-center text-xs text-slate-500">
        🔒 Your data is processed temporarily and never stored.
      </p>
    </div>
  </div>
  </SignedIn>
  <SignedOut>
    <RedirectToSignIn />
  </SignedOut>
</template>

<style scoped>
@keyframes pop {
  0% { transform: scale(0.6); opacity: 0 }
  60% { transform: scale(1.2) }
  100% { transform: scale(1); opacity: 1 }
}
.animate-pop {
  animation: pop 0.5s ease-out;
}
</style>
