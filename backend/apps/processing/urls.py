from django.urls import path
from .views import start_processing

urlpatterns = [
    path("start/", start_processing),
]
