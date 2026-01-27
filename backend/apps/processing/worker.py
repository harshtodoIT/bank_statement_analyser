import threading
from decimal import Decimal
from django.conf import settings
from django.db import transaction

from apps.parsing.dispatcher import parse_statement
from apps.structuring.engine import structure_rows
from apps.validation.engine import validate_transactions
from apps.computation.services import compute_all
from apps.categorization.engine import categorize_transactions

from .models import ProcessingJob
from .cleanup import delete_folder

from apps.results.models import ProcessingResult
from apps.statements.models import Statement
from apps.transactions.models import Transaction


def start_async_job(job_id):
    thread = threading.Thread(target=run_processing_job, args=(job_id,))
    thread.daemon = True
    thread.start()


def _cleanup_if_temporary(job):
    try:
        profile = job.user.profile
    except Exception:
        return

    if profile.data_retention_preference == "TEMPORARY":
        tmp_root = settings.MEDIA_ROOT / "tmp" / job.session_id
        delete_folder(tmp_root)


def _persist_statement_and_transactions(
    job,
    structured_transactions,
    original_file_name,
):
    """
    Persist statement + transactions atomically.
    Duplicate file_hash for same user is rejected.
    """

    # ❌ Duplicate protection (choice B)
    if Statement.objects.filter(
        user=job.user,
        file_hash=job.file_hash,
    ).exists():
        raise ValueError("This statement has already been uploaded.")

    dates = [tx["date"] for tx in structured_transactions]
    start_date = min(dates)
    end_date = max(dates)

    with transaction.atomic():
        statement = Statement.objects.create(
            user=job.user,
            bank_name=job.bank_name,
            file_name=original_file_name,
            file_hash=job.file_hash,
            start_date=start_date,
            end_date=end_date,
        )

        tx_objects = []
        for tx in structured_transactions:
            tx_objects.append(
                Transaction(
                    statement=statement,
                    user=job.user,
                    date=tx["date"],
                    description=tx["description"],
                    debit=tx.get("debit"),
                    credit=tx.get("credit"),
                    balance=tx["balance"],
                    category=tx.get("category"),
                    category_confidence=tx.get("confidence"),
                )
            )

        Transaction.objects.bulk_create(tx_objects)


def run_processing_job(job_id):
    try:
        job = ProcessingJob.objects.get(id=job_id)
        job.status = ProcessingJob.Status.PROCESSING
        job.save(update_fields=["status"])

        session_id = job.session_id
        tmp_root = settings.MEDIA_ROOT / "tmp" / session_id

        file_path = None
        original_file_name = None

        for f in tmp_root.iterdir():
            if f.is_file():
                file_path = f
                original_file_name = f.name
                break

        if not file_path:
            raise ValueError("Uploaded file not found for processing")

        # ---- PIPELINE ----
        raw_rows = parse_statement(str(file_path))
        structured_transactions = structure_rows(raw_rows)
        validate_transactions(structured_transactions)

        computed = compute_all(structured_transactions)
        category_data = categorize_transactions(structured_transactions)
        # ✅ Inject bank_name into each transaction snapshot
        for tx_list in category_data["transactions"].values():
            for tx in tx_list:
                tx["bank_name"] = job.bank_name
                
        total_transactions = len(structured_transactions)

        # ---- PERSIST IF REQUIRED ----
        if job.privacy_mode == ProcessingJob.PrivacyMode.PERSIST:
            _persist_statement_and_transactions(
                job,
                structured_transactions,
                original_file_name,
            )

        # ---- RESULT SNAPSHOT ----
        ProcessingResult.objects.create(
            job_id=job.id,
            user=job.user,
            status="SUCCESS",
            totals=computed["totals"],
            monthly_summary=computed["monthly_summary"],
            net_cash_flow=computed["net_cash_flow"],
            categorized_summary=category_data["summary"],
            categorized_transactions=category_data["transactions"],  # ✅
            total_transactions=total_transactions,
            bank_name=job.bank_name,
        )


        job.status = ProcessingJob.Status.SUCCESS
        job.save(update_fields=["status"])

        _cleanup_if_temporary(job)

    except Exception as e:
        try:
            ProcessingResult.objects.create(
                job_id=job.id,
                user=job.user,
                status="FAILED",
                error=str(e),
                categorized_summary={},
                total_transactions=0,
                bank_name=job.bank_name,
            )

            job.status = ProcessingJob.Status.FAILED
            job.error_message = str(e)
            job.save(update_fields=["status", "error_message"])

            _cleanup_if_temporary(job)
        except Exception:
            pass
