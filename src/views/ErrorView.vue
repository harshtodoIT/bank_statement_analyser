<template>
  <div class="min-h-screen flex items-center justify-center bg-red-50">
    <div class="bg-white p-8 rounded-xl shadow-md text-center max-w-md">

      <h1 class="text-xl font-semibold text-red-600">
        Upload Failed
      </h1>

      <p class="text-sm text-gray-600 mt-3">
        The file could not be processed. Please check the error message and try again.
      </p>

      <button
        class="mt-6 bg-red-600 text-white px-4 py-2 rounded-md hover:bg-red-700"
        @click="$router.push('/')"
      >
        Re-upload Statement
      </button>

    </div>
  </div>
</template>
