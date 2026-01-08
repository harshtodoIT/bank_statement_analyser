<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-sky-50 to-blue-100 px-4">
    <div class="w-full max-w-lg rounded-2xl bg-white shadow-xl p-8">

      <!-- Icon -->
      <div class="flex justify-center mb-4">
        <div class="h-14 w-14 flex items-center justify-center rounded-full bg-blue-600 text-white">
          📄
        </div>
      </div>

      <!-- Heading -->
      <h1 class="text-2xl font-semibold text-center text-gray-900">
        Bank Statement Analyser
      </h1>
      <p class="text-center text-gray-500 mt-1">
        Upload your bank statement for instant analysis
      </p>

      <!-- Upload Box -->
      <div
        class="mt-6 rounded-xl border-2 border-dashed border-blue-300 bg-blue-50/50 p-8 text-center"
      >
        <div class="mx-auto mb-4 flex h-14 w-14 items-center justify-center rounded-full bg-blue-100 text-blue-600 text-2xl">
          ⬆️
        </div>

        <p class="font-medium text-gray-800">
          Drag & Drop your file here
        </p>
        <p class="text-sm text-gray-500 mt-1">or</p>

        <button
          class="mt-4 rounded-lg bg-blue-600 px-6 py-2 text-white font-medium hover:bg-blue-700 transition"
        >
          Browse Files
        </button>

        <p class="mt-3 text-xs text-gray-500">
          Supported formats: PDF, PNG, JPG, Excel (Max 10MB)
        </p>
      </div>

      <!-- Analyze Button -->
      <button
        class="mt-6 w-full rounded-lg bg-gray-300 py-3 font-semibold text-gray-600 cursor-not-allowed"
      >
        Analyze Statement
      </button>

      <!-- Privacy -->
      <p class="mt-4 text-center text-xs text-gray-500">
        🔒 Your data is processed securely and never stored
      </p>

    </div>
  </div>
</template>
