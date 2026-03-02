<script setup>
import { SignedOut, SignedIn, SignInButton, SignUpButton } from "@clerk/vue"
import { useRouter } from "vue-router"

const router = useRouter()
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-slate-950 via-slate-900 to-slate-800 px-4">

    <!-- ✅ If user is signed in → redirect immediately -->
    <SignedIn>
      <div v-if="router.push('/upload')" />
    </SignedIn>

    <!-- ❌ If user is signed out → show login buttons -->
    <SignedOut>
      <div class="w-full max-w-md bg-slate-800/70 backdrop-blur-xl border border-slate-700 rounded-2xl shadow-2xl p-10 text-center">

        <div class="mb-8">
          <h1 class="text-3xl font-bold text-white tracking-tight">
            Bank Statement Analyser
          </h1>
          <p class="text-slate-400 mt-2 text-sm">
            Smart insights from your financial data
          </p>
        </div>

        <div class="h-px bg-slate-700 mb-6"></div>

        <div class="flex flex-col gap-4">
          <SignInButton
            mode="redirect"
            redirect-url="/upload"
            class="w-full bg-emerald-500 hover:bg-emerald-600 text-white font-medium py-2.5 rounded-lg transition-all duration-200 shadow-md hover:shadow-emerald-500/20"
          />

          <SignUpButton
            mode="redirect"
            redirect-url="/upload"
            class="w-full bg-slate-700 hover:bg-slate-600 text-white font-medium py-2.5 rounded-lg transition-all duration-200 border border-slate-600"
          />
        </div>

        <p class="text-xs text-slate-500 mt-8">
          Secure authentication powered by Clerk
        </p>

      </div>
    </SignedOut>

  </div>
</template>
