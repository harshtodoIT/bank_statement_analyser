from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from apps.statements.models import Statement
from apps.results.models import ProcessingResult
from apps.privacy.permissions import HasPrivacyPreference


@api_view(["GET"])
@permission_classes([IsAuthenticated, HasPrivacyPreference])
def list_statements(request):
    """
    List all persisted statements for the authenticated user.
    """
    statements = (
        Statement.objects
        .filter(user=request.user)
        .order_by("-uploaded_at")
    )

    response = []

    for stmt in statements:
        result = ProcessingResult.objects.filter(
            user=request.user,
            bank_name=stmt.bank_name,
            job_id__isnull=False,
        ).order_by("-created_at").first()

        response.append({
            "id": stmt.id,
            "bank_name": stmt.bank_name,
            "start_date": stmt.start_date,
            "end_date": stmt.end_date,
            "uploaded_at": stmt.uploaded_at,
            "total_transactions": stmt.transactions.count(),
            "net_cash_flow": result.net_cash_flow if result else None,
        })

    return Response(
        {
            "status": "SUCCESS",
            "data": response,
        },
        status=status.HTTP_200_OK,
    )

@api_view(["GET"])
@permission_classes([IsAuthenticated, HasPrivacyPreference])
def statement_detail(request, statement_id):
    """
    Detailed view of a single persisted statement.
    """
    statement = Statement.objects.filter(
        id=statement_id,
        user=request.user,
    ).first()

    if not statement:
        return Response(
            {"error": "Statement not found"},
            status=status.HTTP_404_NOT_FOUND,
        )

    result = (
        ProcessingResult.objects
        .filter(
            user=request.user,
            bank_name=statement.bank_name,
        )
        .order_by("-created_at")
        .first()
    )

    return Response(
        {
            "status": "SUCCESS",
            "data": {
                "id": statement.id,
                "bank_name": statement.bank_name,
                "file_name": statement.file_name,
                "start_date": statement.start_date,
                "end_date": statement.end_date,
                "uploaded_at": statement.uploaded_at,
                "total_transactions": statement.transactions.count(),
                "totals": result.totals if result else None,
                "monthly_summary": result.monthly_summary if result else None,
                "category_summary": result.categorized_summary if result else None,
                "net_cash_flow": result.net_cash_flow if result else None,
            },
        },
        status=status.HTTP_200_OK,
    )
