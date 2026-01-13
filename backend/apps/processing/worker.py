import threading
from apps.parsing.dispatcher import parse_statement
from apps.structuring.engine import structure_rows
from .models import ProcessingJob
from apps.validation.engine import validate_transactions
from apps.results.models import ProcessingResult
from apps.computation.services import compute_all


def start_async_job(job_id):
    """Start the processing job in a separate thread."""
    thread = threading.Thread(target=run_processing_job, args=(job_id,))
    thread.daemon = True
    thread.start()


def run_processing_job(job_id):
    try:
        job = ProcessingJob.objects.get(id=job_id)
        job.status = ProcessingJob.Status.PROCESSING
        job.save()

        # Get file path from session temp storage
        # Phase 1 assumption: one file per session
        from django.conf import settings
        from pathlib import Path

        session_id = job.session_id
        tmp_root = settings.MEDIA_ROOT / "tmp" / session_id

        file_path = None
        for f in tmp_root.iterdir():
            if f.is_file():
                file_path = f
                break

        if not file_path:
            raise ValueError("Uploaded file not found for processing")

        # Step 1: Parse raw rows
        raw_rows = parse_statement(str(file_path))

        # Step 2: Structure rows (STRICT)
        structured_transactions = structure_rows(raw_rows)

        # Step 3: Validate transactions (STRICT)
        validate_transactions(structured_transactions)

        # Phase 1: we do not persist results yet
        # Success means structuring passed completely
        computed = compute_all(structured_transactions)

        ProcessingResult.objects.create(
            job_id=job.id,
            status="SUCCESS",
            totals=computed["totals"],
            monthly_summary=computed["monthly_summary"],
            net_cash_flow=computed["net_cash_flow"],
        )

        job.status = ProcessingJob.Status.SUCCESS
        job.save()

    except Exception as e:
        try:
            ProcessingResult.objects.create(
                job_id=job.id,
                status="FAILED",
                error=str(e),
            )

            job.status = ProcessingJob.Status.FAILED
            job.error_message = str(e)
            job.save()
        except Exception:
            pass
