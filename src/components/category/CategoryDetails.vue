<script setup>
  import { computed } from "vue";
  import { useDashboardStore } from "../../stores/dashboard.store";
  import CategorySection from "./CategorySection.vue";

  const store = useDashboardStore();

  const incomeTotal = computed(() =>
    store.incomeCategories.reduce((s, c) => s + c.amount, 0)
  );

  const expenseTotal = computed(() =>
    store.expenseCategories.reduce((s, c) => s + c.amount, 0)
  );

  const uncategorizedTotal = computed(() =>
    store.uncategorizedAmount || 0
  );
  </script>

  <template>
    <div class="space-y-8">
      <CategorySection
        title="Income Categories"
        :total="incomeTotal"
        :categories="store.incomeCategories"
        type="income"
      />

      <CategorySection
        title="Expense Categories"
        :total="expenseTotal"
        :categories="store.expenseCategories"
        type="expense"
      />

      <CategorySection
        title="Uncategorized Transactions"
        :total="uncategorizedTotal"
        :categories="
          store.uncategorizedAmount
            ? [{ name: 'Uncategorized', amount: store.uncategorizedAmount }]
            : []
        "
        type="uncategorized"
      />
    </div>
  </template>
