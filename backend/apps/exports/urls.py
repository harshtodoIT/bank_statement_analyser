from django.urls import path
from .views import export_csv, export_pdf

urlpatterns = [
    path("export/csv/<uuid:job_id>/", export_csv),
    path("export/pdf/<uuid:job_id>/", export_pdf),
]