import threading
from apps.parsing.dispatcher import parse_statement
from apps.structuring.engine import structure_rows
from .models import ProcessingJob
from apps.validation.engine import validate_transactions
from apps.results.models import ProcessingResult
from apps.computation.services import compute_all
from apps.categorization.engine import categorize_transactions


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

        # Locate uploaded file (one file per session)
        from django.conf import settings

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

        # Step 2: Structure rows
        structured_transactions = structure_rows(raw_rows)

        # Step 3: Validate transactions
        validate_transactions(structured_transactions)

        # Step 4: Compute summaries
        computed = compute_all(structured_transactions)
        category_summary = categorize_transactions(structured_transactions)

        # ✅ Total transactions count
        total_transactions = len(structured_transactions)

        # Persist final result
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

    except Exception as e:
        try:
            ProcessingResult.objects.create(
                job_id=job.id,
                status="FAILED",
                error=str(e),
                categorized_summary={},
                total_transactions=0,
                bank_name=job.bank_name,
            )

            job.status = ProcessingJob.Status.FAILED
            job.error_message = str(e)
            job.save()
        except Exception:
            pass
