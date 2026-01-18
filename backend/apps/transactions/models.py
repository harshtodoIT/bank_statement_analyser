from django.core.exceptions import ValidationError
from django.db import models
from apps.statements.models import Statement
from django.conf import settings


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

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="transactions",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Exactly one of debit or credit must be present
        if self.debit and self.credit:
            raise ValidationError("Transaction cannot have both debit and credit.")

        if not self.debit and not self.credit:
            raise ValidationError("Transaction must have either debit or credit.")

        # Amounts must be non-negative
        if self.debit is not None and self.debit < 0:
            raise ValidationError("Debit amount cannot be negative.")

        if self.credit is not None and self.credit < 0:
            raise ValidationError("Credit amount cannot be negative.")

        # Balance must be non-negative
        if self.balance < 0:
            raise ValidationError("Balance cannot be negative.")

        # AI confidence must be between 0 and 1
        if self.category_confidence is not None:
            if not (0 <= self.category_confidence <= 1):
                raise ValidationError("Category confidence must be between 0 and 1.")

    def save(self, *args, **kwargs):
        # Ensure clean() is always called
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.date} | {self.description[:40]}"
