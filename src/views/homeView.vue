<script setup>
  import { SignedIn, SignedOut, SignInButton, SignUpButton } from "@clerk/vue"
  import { useRouter } from "vue-router"
  import { ref, onMounted } from "vue"
  
  const router = useRouter()
  const isDark = ref(false)
  
  function goToUpload() {
    router.replace("/upload")
  }
  
  function toggleTheme() {
    isDark.value = !isDark.value
    document.documentElement.classList.toggle("dark", isDark.value)
  }
  
  onMounted(() => {
    document.documentElement.classList.remove("dark")
  })
  </script>
  
  <template>
    <div
      class="min-h-screen relative flex items-center justify-center overflow-hidden
             bg-[#F9FAFB] dark:bg-gray-900"
    >
  
      <!-- theme toggle -->
      <button
        @click="toggleTheme"
        class="absolute top-6 right-6 rounded-full border border-gray-300
               bg-white/80 backdrop-blur px-3 py-1.5 text-xs font-medium
               text-gray-700 hover:bg-gray-100
               dark:bg-gray-800 dark:text-gray-200 dark:border-gray-700"
      >
        {{ isDark ? "Light" : "Dark" }}
      </button>
  
      <!-- soft brand background blobs -->
      <div class="absolute -top-32 -left-32 h-96 w-96 rounded-full bg-purple-100 blur-3xl opacity-60 dark:opacity-30"></div>
      <div class="absolute top-1/3 -right-32 h-96 w-96 rounded-full bg-blue-100 blur-3xl opacity-60 dark:opacity-30"></div>
      <div class="absolute bottom-[-8rem] left-1/3 h-80 w-80 rounded-full bg-cyan-100 blur-3xl opacity-50 dark:opacity-25"></div>
  
      <!-- glass card -->
      <div
        class="relative w-full max-w-sm rounded-2xl p-8 text-center
               border border-white/40 bg-white/70 backdrop-blur-xl shadow-xl
               dark:bg-gray-800/70 dark:border-gray-700"
      >
  
        <SignedOut>
          <div class="mb-6">
            <h1 class="text-2xl font-semibold text-gray-900 dark:text-gray-100">
              Welcome
            </h1>
            <p class="mt-1 text-sm text-gray-500 dark:text-gray-400">
              Track income and expenses clearly
            </p>
          </div>
  
          <div class="flex flex-col gap-3">
            <SignInButton
              class="w-full py-2.5 rounded-xl bg-purple-500 text-white font-medium
                     hover:bg-purple-600 transition"
            />
            <SignUpButton
              class="w-full py-2.5 rounded-xl border border-gray-300 bg-white/60
                     text-gray-700 hover:bg-gray-100 transition
                     dark:bg-gray-700 dark:text-gray-200 dark:border-gray-600"
            />
          </div>
  
          <div class="mt-6 flex items-center justify-center gap-2 text-xs text-gray-400 dark:text-gray-500">
            <span class="h-px w-10 bg-gray-200 dark:bg-gray-700"></span>
            <span>Secure • Private • No ads</span>
            <span class="h-px w-10 bg-gray-200 dark:bg-gray-700"></span>
          </div>
        </SignedOut>
  
        <SignedIn>
          <div class="flex flex-col items-center gap-3">
            <div class="h-10 w-10 rounded-full bg-purple-100/80 flex items-center justify-center dark:bg-purple-900/40">
              <div class="h-4 w-4 rounded-full bg-purple-500 animate-pulse"></div>
            </div>
            <p class="text-sm font-medium text-gray-600 dark:text-gray-300">
              Redirecting to dashboard
            </p>
            {{ goToUpload() }}
          </div>
        </SignedIn>
  
      </div>
    </div>
  </template>
  