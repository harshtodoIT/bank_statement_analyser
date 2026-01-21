<script setup>
  import { useRoute } from "vue-router"

  defineEmits(["toggle"])
  const route = useRoute()
  </script>

  <template>
    <header
      class="hidden lg:flex h-16 items-center
             border-b bg-white px-6"
    >
    <button
      class="p-2 rounded hover:bg-gray-100 lg:hidden"
      @click="toggleMobile"
    >
      ☰
    </button>


      <h1 class="text-2xl font-bold text-gray-900">
        {{ route.meta?.title }}
      </h1> 
    </header>
  </template>
