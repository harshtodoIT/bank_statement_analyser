<template>
  <div
    class="min-h-screen py-12 px-4
           bg-gradient-to-br from-[#0b1220] via-[#0e1628] to-[#111827]"
  >
    <div class="max-w-3xl mx-auto space-y-8">

      <!-- PAGE HEADING -->
      <div class="text-center">
        <h1 class="text-2xl font-semibold text-white">
          Statement Processing Failed
        </h1>
        <p class="text-slate-400 mt-1 text-sm">
          Don’t worry — your data is safe and was not stored.
        </p>
      </div>

      <!-- MAIN ERROR CARD -->
      <div
        class="bg-slate-900/80 backdrop-blur-xl
               border border-white/10
               rounded-2xl shadow-xl p-8
               text-center max-w-md mx-auto"
      >
        <!-- ICON -->
        <div
          class="w-16 h-16 mx-auto flex items-center justify-center
                 rounded-full bg-orange-500/20"
        >
          <span class="text-orange-400 text-2xl">⚠️</span>
        </div>

        <!-- STATUS BADGE -->
        <span
          class="inline-block mt-4 px-3 py-1 text-xs rounded-full
                 bg-orange-500/10 text-orange-400"
        >
          Rejected File
        </span>

        <!-- TITLE -->
        <h2 class="text-lg font-semibold text-white mt-4">
          Unsupported File Format
        </h2>

        <!-- DESCRIPTION -->
        <p class="text-sm text-slate-400 mt-2">
          The uploaded file format is not supported.
          Please upload a PDF or image file from a recognized bank.
        </p>

        <!-- ACTION BUTTONS -->
        <div class="mt-6 flex gap-3 justify-center">

          <!-- Re-upload -->
          <button
            class="px-4 py-2 rounded-lg text-sm
                   border border-indigo-400/40 text-indigo-300
                   hover:bg-indigo-500/10 transition"
            @click="$router.back()"
          >
            Re-upload Statement
          </button>

          <!-- Upload Different -->
          <button
            class="px-4 py-2 rounded-lg text-sm
                   bg-indigo-600 text-white
                   hover:bg-indigo-700 transition"
            @click="$router.push('/upload')"
          >
            Upload Different File
          </button>
        </div>
      </div>

      <!-- SECURITY NOTE -->
      <p class="text-center text-xs text-slate-500">
        🔒 No financial data was stored or shared.
      </p>

      <!-- ERROR DETAILS -->
      <div
        class="bg-slate-900/80 backdrop-blur-xl
               border border-white/10
               rounded-2xl shadow-lg p-6
               max-w-2xl mx-auto"
      >
        <h3 class="text-lg font-semibold text-white mb-4">
          Error Details
        </h3>

        <div class="divide-y divide-white/10 text-sm">
          <div class="flex justify-between py-3">
            <span class="text-slate-400">Failure Reason</span>
            <span class="text-red-400 font-medium">
              Unsupported bank format
            </span>
          </div>

          <div class="flex justify-between py-3">
            <span class="text-slate-400">Processing Stage</span>
            <span class="text-slate-200">
              Format Validation
            </span>
          </div>
        </div>
      </div>

      <!-- COMMON REASONS -->
      <div
        class="bg-slate-900/80 backdrop-blur-xl
               border border-white/10
               rounded-2xl shadow-lg p-6
               max-w-2xl mx-auto"
      >
        <h3 class="text-lg font-semibold text-white mb-4">
          Common Rejection Reasons
        </h3>

        <ul class="space-y-2 text-sm text-slate-300 list-disc pl-5">
          <li>Unsupported bank format</li>
          <li>Corrupted or scanned image PDF</li>
          <li>Password-protected file</li>
          <li>Missing transaction data</li>
        </ul>
      </div>

    </div>
  </div>
</template>
