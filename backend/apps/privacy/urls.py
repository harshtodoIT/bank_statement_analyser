from django.urls import path
from .views import privacy_status, choose_privacy

urlpatterns = [
    path("privacy/status/", privacy_status),
    path("privacy/choose/", choose_privacy),
]
