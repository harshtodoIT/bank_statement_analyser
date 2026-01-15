<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 px-4">
    <div class="w-full max-w-2xl bg-white rounded-xl shadow-md p-8">

      <!-- Title -->
      <h1 class="text-2xl font-semibold text-gray-900 text-center">
        Processing Your Statement
      </h1>
      <p class="text-gray-500 text-center mt-2">
        This may take a few moments. Please don't refresh or close the page.
      </p>

      <!-- Progress -->
      <div class="mt-6">
        <div class="flex justify-between text-sm text-gray-600 mb-1">
          <span>Progress</span>
          <span>{{ progress }}% Complete</span>
        </div>
        <div class="w-full bg-gray-200 rounded-full h-2">
          <div
            class="bg-blue-600 h-2 rounded-full transition-all duration-500"
            :style="{ width: progress + '%' }"
          ></div>
        </div>
      </div>

      <!-- Steps -->
      <div class="mt-6 space-y-4">
        <div
          v-for="step in steps"
          :key="step.key"
          class="flex items-center gap-4 p-4 rounded-lg border"
          :class="step.status === 'done'
            ? 'bg-green-50 border-green-200'
            : 'bg-blue-50 border-blue-200'"
        >
          <!-- Icon -->
          <div
            class="w-10 h-10 flex items-center justify-center rounded-full"
            :class="step.status === 'done'
              ? 'bg-green-500 text-white'
              : 'bg-blue-500 text-white'"
          >
            <!-- Done -->
            <span v-if="step.status === 'done'">✔</span>

            <!-- Loading -->
            <svg
              v-else
              class="w-5 h-5 animate-spin text-white"
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

          <!-- Text -->
          <p class="font-medium text-gray-800">
            {{ step.label }}
          </p>
        </div>
      </div>

      <!-- Status message -->
      <div class="mt-6 bg-blue-50 border border-blue-200 rounded-lg p-4 flex items-center gap-3">
        <svg
          class="w-4 h-4 animate-spin text-blue-500"
          viewBox="0 0 24 24"
        >
          <circle
            class="opacity-20"
            cx="12"
            cy="12"
            r="10"
            stroke="currentColor"
            stroke-width="2"
            fill="none"
          />
          <path
            d="M22 12a10 10 0 01-10 10"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            fill="none"
          />
        </svg>

        <p class="text-blue-700">
          Finalizing analysis and preparing results...
        </p>
      </div>

      <!-- Actions -->
      <div class="mt-6 flex justify-center gap-6">
        <button
          disabled
          class="px-6 py-2 rounded-lg bg-blue-600 text-white opacity-70 cursor-not-allowed"
        >
          Analyzing...
        </button>

        <button
          class="text-gray-500 hover:text-gray-700 text-sm underline"
        >
          Cancel & Re-upload
        </button>
      </div>

    </div>
  </div>
</template>

<script setup>
  import { ref } from "vue";

  const progress = ref(10);

  const steps = ref([
    { key: "upload", label: "Uploading file", status: "done" },
    { key: "read", label: "Reading PDF", status: "done" },
    { key: "extract", label: "Extracting transactions", status: "loading" },
    { key: "categorize", label: "Categorizing data", status: "pending" },
    { key: "finalize", label: "Finalizing analysis", status: "pending" },
  ]);
  import { onMounted, onUnmounted } from "vue";
  import { useRouter } from "vue-router";
  import { useProcessingStore } from "../stores/processing.store";

  const processingStore = useProcessingStore();
  const router = useRouter();

  let timer = null;

  onMounted(async () => {
    try {
      await processingStore.startJob();
    } catch {
      router.push("/upload");
      return;
    }

    timer = setInterval(async () => {
      await processingStore.pollStatus();

      if (processingStore.status === "SUCCESS") {
        clearInterval(timer);
        router.push("/dashboard");
      }

      if (processingStore.status === "FAILED") {
        clearInterval(timer);
        console.error(processingStore.error);
      }

      if (processingStore.status === "PROCESSING") {
        progress.value = 60;
      }

      if (processingStore.status === "SUCCESS") {
        progress.value = 100;
      }

    }, 2000);
  });

  onUnmounted(() => {
    if (timer) clearInterval(timer);
  });

</script>
