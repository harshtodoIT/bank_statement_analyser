from django.conf import settings
from django.db import models
from apps.statements.models import Statement


class ManualAdjustment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="manual_adjustments",
    )

    statement = models.ForeignKey(
        Statement,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="manual_adjustments",
    )

    label = models.CharField(max_length=255)

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    note = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.label} | {self.amount}"
