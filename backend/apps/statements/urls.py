from django.urls import path
from .views import list_statements, statement_detail

urlpatterns = [
    path("statements/", list_statements),
    path("statements/<int:statement_id>/", statement_detail),
]
