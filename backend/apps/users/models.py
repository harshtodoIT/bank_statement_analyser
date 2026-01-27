from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    clerk_user_id = models.CharField(
        max_length=255,
        unique=True,
        db_index=True,
    )

    DATA_RETENTION_CHOICES = [
        ("TEMPORARY", "Temporary"),
        ("PERSIST", "Persist"),
    ]

    data_retention_preference = models.CharField(
        max_length=20,
        choices=DATA_RETENTION_CHOICES,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.clerk_user_id}"
