import time
import threading
from .models import ProcessingJob
from django.http import JsonResponse


def run_processing_job(job_id):
    try:
        job = ProcessingJob.objects.get(id=job_id)
        job.status = ProcessingJob.Status.PROCESSING
        job.save()

        # Simulate heavy processing
        time.sleep(5)

        # Simulate success
        job.status = ProcessingJob.Status.SUCCESS
        job.save()

    except Exception as e:
        try:
            job = ProcessingJob.objects.get(id=job_id)
            job.status = ProcessingJob.Status.FAILED
            job.error_message = str(e)
            job.save()
        except Exception:
            pass


def start_async_job(job_id):
    thread = threading.Thread(
        target=run_processing_job,
        args=(job_id,),
        daemon=True
    )
    thread.start()
