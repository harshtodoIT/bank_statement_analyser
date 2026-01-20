<script setup>
  import { SignedIn, SignedOut, SignInButton, SignUpButton } from "@clerk/vue"
  import { useRouter } from "vue-router"

  const router = useRouter()

  function goToUpload() {
    router.replace("/upload")
  }
  </script>

  <template>
    <div>
      <SignedOut>
        <SignInButton />
        <SignUpButton />
      </SignedOut>

      <SignedIn>
        <p>Redirecting...</p>
        {{ goToUpload() }}
      </SignedIn>
    </div>
  </template>
