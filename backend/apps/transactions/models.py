from django.db import models
from apps.statements.models import Statement


class Transaction(models.Model):
    statement = models.ForeignKey(
        Statement,
        on_delete=models.CASCADE,
        related_name="transactions",
    )

    date = models.DateField()
    description = models.TextField()

    debit = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )

    credit = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True,
    )

    balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    category = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    category_confidence = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} | {self.description[:40]}"
