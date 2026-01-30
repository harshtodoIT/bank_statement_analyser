<script setup>
import { SignedOut, SignInButton, SignUpButton } from "@clerk/vue"
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-slate-900">
    <SignedOut>
      <div class="bg-white p-8 rounded-xl text-center">
        <h1 class="text-xl font-semibold mb-4">Login</h1>
        <SignInButton class="mb-2" />
        <SignUpButton />
      </div>
    </SignedOut>
  </div>
</template>
