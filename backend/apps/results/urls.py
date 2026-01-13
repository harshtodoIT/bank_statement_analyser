from django.urls import path
from .views import get_summary

urlpatterns = [
    path("summary/<uuid:job_id>/", get_summary),
]