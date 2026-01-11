from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models

class Statement(models.Model):
    BANK_CHOICES = [
        ("HDFC", "HDFC Bank"),
        ("ICICI", "ICICI Bank"),
        ("SBI", "SBI Bank"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="statements",
    )

    bank_name = models.CharField(
        max_length=10,
        choices=BANK_CHOICES,
    )

    file_name = models.CharField(max_length=255)
    file_hash = models.CharField(max_length=64)

    start_date = models.DateField()
    end_date = models.DateField()

    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["file_hash"]),
        ]

    def __str__(self):
        return f"{self.bank_name} | {self.start_date} → {self.end_date}"
