from django.urls import path
from .views import start_processing, process_status
from .views_history import processing_history

urlpatterns = [
    path("start/", start_processing),
    path("status/<uuid:job_id>/", process_status),
    path("history/", processing_history),
]
