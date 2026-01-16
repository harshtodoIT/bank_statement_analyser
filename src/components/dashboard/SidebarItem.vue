<script setup>
  defineProps({
    label: String,
    isOpen: Boolean
  })
  </script>

  <template>
    <div class="relative group w-full">
      <slot />

      <!-- Tooltip (only when collapsed) -->
      <teleport to="body">
        <div
          v-if="!isOpen"
          class="fixed z-[99999] pointer-events-none
                 opacity-0 group-hover:opacity-100 transition
                 bg-gray-900 text-white text-xs px-3 py-1.5 rounded-md shadow-lg"
          :style="{
            top: `${$el?.getBoundingClientRect().top + 10}px`,
            left: `${$el?.getBoundingClientRect().right + 12}px`
          }"
        >
          {{ label }}
        </div>
      </teleport>
    </div>
  </template>
