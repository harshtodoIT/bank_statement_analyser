from django.urls import path
from .views import get_report

urlpatterns = [
    path("report/<uuid:job_id>/", get_report),
]