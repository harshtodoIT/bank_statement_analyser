<template>
  <div class="min-h-screen bg-gray-50 py-12">
    <div class="max-w-3xl mx-auto space-y-6">

      <!-- Page Heading -->
      <div class="text-center">
        <h1 class="text-2xl font-semibold text-blue-700">
          Statement Processing Failed
        </h1>
        <p class="text-gray-500 mt-1">
          Don’t worry — your data is safe.
        </p>
      </div>

      <!-- Main Card -->
      <div class="bg-white rounded-xl shadow-sm p-8 text-center max-w-md mx-auto">

        <!-- Warning Icon -->
        <div class="w-16 h-16 mx-auto flex items-center justify-center rounded-full bg-orange-100">
          <span class="text-orange-500 text-2xl">⚠️</span>
        </div>

        <!-- Status Badge -->
        <span class="inline-block mt-4 px-3 py-1 text-xs rounded-full bg-orange-100 text-orange-600">
          Rejected File
        </span>

        <!-- Title -->
        <h2 class="text-lg font-semibold text-gray-800 mt-4">
          Unsupported File Format
        </h2>

        <!-- Description -->
        <p class="text-sm text-gray-600 mt-2">
          The uploaded file format is not supported.
          Please upload a PDF or image file from a recognized bank.
        </p>

        <!-- ACTION BUTTONS -->
        <div class="mt-6 flex gap-3 justify-center">

          <!-- Re-upload same file -->
          <button
            class="px-4 py-2 rounded-md border border-blue-600 text-blue-600 hover:bg-blue-50"
            @click="$router.back()"
          >
            Re-upload Statement
          </button>

          <!-- Upload different file -->
          <button
            class="px-4 py-2 rounded-md bg-blue-600 text-white hover:bg-blue-700"
            @click="$router.push('/upload')"
          >
            Upload Different File
          </button>

        </div>
      </div>

      <!-- Footer note -->
      <p class="text-center text-xs text-gray-400 mt-6">
        🔒 No financial data was stored or shared.
      </p>

      <!-- Error Details -->
      <div class="bg-white rounded-xl shadow-sm p-6 mt-8 max-w-2xl mx-auto text-left">
        <h3 class="text-lg font-semibold text-blue-700 mb-4">
          Error Details
        </h3>

        <div class="divide-y text-sm">
          <div class="flex justify-between py-3">
            <span class="text-gray-500">Failure Reason</span>
            <span class="text-red-600 font-medium">
              Unsupported bank format
            </span>
          </div>

          <div class="flex justify-between py-3">
            <span class="text-gray-500">Processing Stage</span>
            <span class="text-gray-800">
              Format Validation
            </span>
          </div>
        </div>
      </div>

      <!-- Common Reasons -->
      <div class="bg-white rounded-xl shadow-sm p-6 mt-8 max-w-2xl mx-auto text-left">
        <h3 class="text-lg font-semibold text-blue-700 mb-4">
          Common Rejection Reasons
        </h3>

        <ul class="space-y-2 text-sm text-gray-700 list-disc pl-5">
          <li>Unsupported bank format</li>
          <li>Corrupted or scanned image PDF</li>
          <li>Password-protected file</li>
          <li>Missing transaction data</li>
        </ul>
      </div>

    </div>
  </div>
</template>
