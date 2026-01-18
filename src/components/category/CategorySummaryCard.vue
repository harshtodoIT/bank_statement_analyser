<script setup>
  defineProps({
    title: String,
    amount: String,
    type: String
  })
  </script>

  <template>
    <div
      class="rounded-xl p-6 border"
      :class="{
        'bg-green-50 border-green-200': type === 'income',
        'bg-red-50 border-red-200': type === 'expense',
        'bg-blue-50 border-blue-200': type === 'balance'
      }"
    >
      <p
        class="text-sm font-medium"
        :class="{
          'text-green-600': type === 'income',
          'text-red-600': type === 'expense',
          'text-blue-600': type === 'balance'
        }"
      >
        {{ title }}
      </p>

      <p
        class="text-2xl font-semibold mt-2"
        :class="{
          'text-green-700': type === 'income',
          'text-red-700': type === 'expense',
          'text-blue-700': type === 'balance'
        }"
      >
        {{ amount }}
      </p>
    </div>
  </template>
