from django.urls import path
from .views import upload_statement

urlpatterns = [
    path('statement/', upload_statement),
]