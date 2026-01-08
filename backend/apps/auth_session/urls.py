from django.urls import path
from .views import ensure_session

urlpatterns = [
    path('session/', ensure_session),
]
