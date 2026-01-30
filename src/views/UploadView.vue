<script setup>
import { ref } from "vue"
import { useRouter } from "vue-router"
import { FileText, CheckCircle } from "lucide-vue-next"
import { useUploadStore } from "../stores/upload.store"

const router = useRouter()
const uploadStore = useUploadStore()

const selectedFile = ref(null)
const isDragging = ref(false)
const isSuccess = ref(false)

const onFileSelect = (event) => {
  const file = event.target.files[0]
  if (!file) return

  selectedFile.value = file
  isSuccess.value = true
}

const onDrop = (event) => {
  event.preventDefault()
  isDragging.value = false

  const file = event.dataTransfer.files[0]
  if (!file) return

  selectedFile.value = file
  isSuccess.value = true
}

const onDragOver = (event) => {
  event.preventDefault()
  isDragging.value = true
}

const onDragLeave = () => {
  isDragging.value = false
}

const goToProcessing = async () => {
  if (!selectedFile.value) return

  const success = await uploadStore.uploadFile(selectedFile.value)
  if (success) {
    router.push("/processing")
  }
}
</script>

<template>
  <div
    class="min-h-screen w-full flex items-center justify-center px-4
           bg-gradient-to-b from-[#0b1220] to-[#111827]"
  >
    <div
      class="w-full max-w-md rounded-2xl p-8
             bg-slate-800/90 border border-white/10
             shadow-2xl backdrop-blur"
    >
      <!-- Icon -->
      <div class="flex justify-center mb-6">
        <div
          class="h-16 w-16 rounded-full flex items-center justify-center
                 shadow-lg transition-all duration-300"
          :class="[
            isSuccess
              ? 'bg-green-500 scale-110'
              : 'bg-gradient-to-br from-indigo-500 to-violet-600 hover:scale-110'
          ]"
        >
          <FileText
            v-if="!isSuccess"
            class="w-9 h-9 text-white"
          />
          <CheckCircle
            v-else
            class="w-9 h-9 text-white animate-bounce"
          />
        </div>
      </div>

      <!-- Title -->
      <h1 class="text-xl font-semibold text-center text-white">
        Bank Statement Analyzer
      </h1>
      <p class="text-sm text-center text-slate-400 mt-1">
        Upload your bank statement for instant analysis
      </p>

      <!-- Upload Box -->
      <div
        class="mt-6 border-2 border-dashed rounded-xl p-6 text-center
               transition-all duration-300"
        :class="[
          isDragging
            ? 'border-indigo-400 bg-indigo-500/10'
            : 'border-white/20 bg-slate-900/40'
        ]"
        @dragover="onDragOver"
        @dragleave="onDragLeave"
        @drop="onDrop"
      >
        <p class="text-sm font-medium text-slate-200">
          Drag & Drop your file here
        </p>

        <p class="text-xs text-slate-400 my-2">or</p>

        <label
          class="inline-block px-4 py-2 rounded-md text-sm transition-all"
          :class="selectedFile
            ? 'bg-slate-700 text-slate-400 cursor-not-allowed'
            : 'bg-indigo-600 text-white hover:bg-indigo-700 cursor-pointer'"
        >
          Browse Files
          <input
            type="file"
            class="hidden"
            :disabled="selectedFile"
            @change="onFileSelect"
          />
        </label>

        <p class="text-xs text-slate-500 mt-3">
          Supported formats: PDF, CSV, Excel
        </p>
      </div>

      <!-- Selected File -->
      <p
        v-if="selectedFile"
        class="text-xs text-center text-slate-300 mt-3"
      >
        Selected file:
        <span class="font-medium">{{ selectedFile.name }}</span>
      </p>

      <!-- Analyze Button -->
      <button
        class="w-full mt-6 py-3 rounded-lg text-sm font-semibold
               transition-all duration-300 active:scale-95"
        :class="selectedFile
          ? 'bg-indigo-600 text-white hover:bg-indigo-700 hover:shadow-lg hover:shadow-indigo-500/30'
          : 'bg-slate-700 text-slate-400 cursor-not-allowed'"
        :disabled="!selectedFile"
        @click="goToProcessing"
      >
        Analyze Statement
      </button>

      <!-- Privacy -->
      <p class="mt-4 text-xs text-center text-slate-500">
        🔒 Your data is processed temporarily in memory and discarded.
      </p>
    </div>
  </div>
</template>
