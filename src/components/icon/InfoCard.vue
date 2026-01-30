<template>
  <div class="bg-white border rounded-xl p-5 hover:shadow transition">
    <div class="flex items-center gap-3 mb-2">
      <slot name="icon" />
      <h3 class="font-semibold">{{ title }}</h3>
    </div>
    <p class="text-gray-600 text-sm">
      <slot />
    </p>
  </div>
</template>
<script setup>
defineProps({
  title: String
})
</script>
