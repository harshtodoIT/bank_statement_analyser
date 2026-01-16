<script setup>
  import CategorySection from './CategorySection.vue'
  </script>

  <template>
    <div class="space-y-8">

      <CategorySection
        title="Income Categories"
        total="6650"
        type="income"
      />

      <CategorySection
        title="Expense Categories"
        total="4150"
        type="expense"
      />

      <CategorySection
        title="Uncategorized Transactions"
        total="485"
        type="uncategorized"
      />

    </div>
  </template>
