<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 to-blue-100">
    <div class="w-full max-w-md bg-white rounded-2xl shadow-lg p-8">

      <!-- Icon -->
      <div class="flex justify-center mb-4">
        <div class="h-12 w-12 flex items-center justify-center rounded-full bg-blue-600 text-white">
          📄
        </div>
      </div>

      <!-- Title -->
      <h1 class="text-xl font-semibold text-center text-gray-800">
        Bank Statement Analyser
      </h1>
      <p class="text-sm text-center text-gray-500 mt-1">
        Upload your bank statement for instant analysis
      </p>

      <!-- Upload box -->
      <div class="mt-6 border-2 border-dashed border-blue-300 rounded-xl p-6 text-center bg-blue-50">
        <p class="text-sm font-medium text-gray-700">
          Drag & Drop your file here
        </p>

        <p class="text-xs text-gray-500 my-2">or</p>

        <label class="cursor-pointer inline-block bg-blue-600 text-white px-4 py-2 rounded-md text-sm hover:bg-blue-700 transition">
          Browse Files
          <input
            type="file"
            class="hidden"
            @change="onFileSelect"
          />
        </label>

        <p class="text-xs text-gray-400 mt-3">
          Supported formats: PDF, CSV, Excel
        </p>
      </div>

      <!-- Selected file -->
      <p v-if="selectedFile" class="text-xs text-center text-gray-600 mt-3">
        Selected file: <b>{{ selectedFile.name }}</b>
      </p>

      <!-- Upload button -->
      <button
        class="w-full mt-6 py-3 rounded-lg text-sm font-semibold transition"
        :class="selectedFile
          ? 'bg-blue-600 text-white hover:bg-blue-700'
          : 'bg-gray-300 text-gray-600 cursor-not-allowed'"
        :disabled="!selectedFile"
        @click="uploadFile"
      >
        Analyze Statement
      </button>

      <!-- Privacy notice (MANDATORY) -->
      <p class="mt-4 text-xs text-center text-gray-500">
        🔒 By default, your data is processed in memory and discarded.
      </p>

    </div>
  </div>
</template>

<script setup>
  import { ref } from "vue"
  import { useRouter } from "vue-router"

  const selectedFile = ref(null)
  const router = useRouter()

  function onFileSelect(event) {
    selectedFile.value = event.target.files[0] || null

    // ❌ No validation
    // ❌ No file reading
    // ✔ Just store file reference
  }

  async function uploadFile() {
    if (!selectedFile.value) return

    const formData = new FormData()
    formData.append("file", selectedFile.value)

    try {
      // move to processing screen immediately
      router.push("/processing")

      await fetch("http://localhost:8000/api/uploads/statement/", {
        method: "POST",
        body: formData,
      })

    } catch (error) {
      console.error("Upload failed", error)
      router.push("/error")
    }
  }
</script>
