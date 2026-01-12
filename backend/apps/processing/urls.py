from django.urls import path
from .views import start_processing, process_status

urlpatterns = [
    path("start/", start_processing),
    path("status/<uuid:job_id>/", process_status),
]
