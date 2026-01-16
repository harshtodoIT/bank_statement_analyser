<template>
  <div class="bg-white rounded-xl shadow p-6">
    <h2 class="text-lg font-semibold mb-4">
      Transactions
    </h2>

    <table class="w-full text-sm">
      <thead>
        <tr class="border-b text-gray-500">
          <th class="py-2 text-left">Date</th>
          <th class="py-2 text-left">Description</th>
          <th class="py-2 text-right">Amount</th>
        </tr>
      </thead>

      <tbody>
        <tr
          v-for="(tx, index) in transactions"
          :key="index"
          class="border-b"
        >
          <td class="py-2">{{ tx.date }}</td>
          <td class="py-2">{{ tx.desc }}</td>
          <td
            class="py-2 text-right font-medium"
            :class="tx.amount > 0 ? 'text-green-600' : 'text-red-500'"
          >
            {{ tx.amount > 0 ? '+' : '' }}₹{{ Math.abs(tx.amount) }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'MonthlyTable',
  props: {
    transactions: Array
  }
}
</script>
