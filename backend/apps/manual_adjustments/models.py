import uuid
from django.conf import settings
from django.db import models

class ManualAdjustment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    result = models.ForeignKey(
        "results.ProcessingResult",
        on_delete=models.CASCADE,
        related_name="manual_adjustments",
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="manual_adjustments",
    )

    label = models.CharField(max_length=100)
    
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    note = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.label} | {self.amount}"