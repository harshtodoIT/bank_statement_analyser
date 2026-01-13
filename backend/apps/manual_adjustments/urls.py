from django.urls import path
from .views import create_manual_adjustment

urlpatterns = [
    path("adjustments/<uuid:job_id>/", create_manual_adjustment),
]