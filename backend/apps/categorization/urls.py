from django.urls import path
from .views import category_drill_down

urlpatterns = [
    path("categorization/drill-down/", category_drill_down),
]
