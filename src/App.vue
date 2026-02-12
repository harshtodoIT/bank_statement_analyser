<script setup>
import { ClerkLoaded, ClerkLoading } from "@clerk/vue"
</script>

<template>
  <!-- While Clerk is initializing -->
  <ClerkLoading>
    <div class="min-h-screen flex items-center justify-center bg-slate-900 text-white">
      <p class="text-lg">Loading...</p>
    </div>
  </ClerkLoading>

  <!-- When Clerk is ready -->
  <ClerkLoaded>
    <router-view />
  </ClerkLoaded>
</template>
