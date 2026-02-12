<template>
  <div class="bg-white border rounded-xl p-5">
    <div class="flex items-start gap-3">
      <slot name="icon" />
      <div>
        <p class="font-medium mb-1">{{ title }}</p>
        <p class="text-sm text-gray-500">
          <slot />
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: String
})
</script>
