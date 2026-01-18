import uuid
from django.db import models


class ProcessingResult(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    categorized_summary = models.JSONField(null=True, blank=True)

    job_id = models.UUIDField(unique=True)
    status = models.CharField(max_length=20)

    totals = models.JSONField(null=True, blank=True)
    monthly_summary = models.JSONField(null=True, blank=True)
    net_cash_flow = models.FloatField(null=True, blank=True)

    total_transactions = models.IntegerField(default=0)
    bank_name = models.CharField(max_length=50, null=True, blank=True)

    error = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job_id} - {self.status}"
