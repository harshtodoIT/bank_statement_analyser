import threading
from django.conf import settings

from apps.parsing.dispatcher import parse_statement
from apps.structuring.engine import structure_rows
from .models import ProcessingJob
from apps.validation.engine import validate_transactions
from apps.results.models import ProcessingResult
from apps.computation.services import compute_all
from apps.categorization.engine import categorize_transactions
from .cleanup import delete_folder

def start_async_job(job_id):
    """Start the processing job in a separate thread."""
    thread = threading.Thread(target=run_processing_job, args=(job_id,))
    thread.daemon = True
    thread.start()


def _cleanup_if_temporary(job):
    """
    Delete uploaded files if user's retention preference is TEMPORARY.
    """
    try:
        profile = job.user.profile
    except Exception:
        return  # No profile, fail-safe: do nothing

    if profile.data_retention_preference == "TEMPORARY":
        tmp_root = settings.MEDIA_ROOT / "tmp" / job.session_id
        delete_folder(tmp_root)


def run_processing_job(job_id):
    try:
        job = ProcessingJob.objects.get(id=job_id)
        job.status = ProcessingJob.Status.PROCESSING
        job.save()

        session_id = job.session_id
        tmp_root = settings.MEDIA_ROOT / "tmp" / session_id

        file_path = None
        for f in tmp_root.iterdir():
            if f.is_file():
                file_path = f
                break

        if not file_path:
            raise ValueError("Uploaded file not found for processing")

        # ---- Processing pipeline ----
        raw_rows = parse_statement(str(file_path))
        structured_transactions = structure_rows(raw_rows)
        validate_transactions(structured_transactions)

        computed = compute_all(structured_transactions)
        category_summary = categorize_transactions(structured_transactions)
        total_transactions = len(structured_transactions)

        ProcessingResult.objects.create(
            job_id=job.id,
            user=job.user,
            status="SUCCESS",
            totals=computed["totals"],
            monthly_summary=computed["monthly_summary"],
            net_cash_flow=computed["net_cash_flow"],
            categorized_summary=category_summary,
            total_transactions=total_transactions,
            bank_name=job.bank_name,
        )

        job.status = ProcessingJob.Status.SUCCESS
        job.save()

        # ✅ ENFORCE PRIVACY
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
            job.save()

            # ✅ ENFORCE PRIVACY EVEN ON FAILURE
            _cleanup_if_temporary(job)

        except Exception:
            pass
