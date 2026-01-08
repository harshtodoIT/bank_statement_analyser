import os
import hashlib
from django.conf import settings


def save_temp_file(file, session_id):
    """
    Saves file to media/tmp/<session_id>/ and returns file path and hash
    """

    tmp_dir = settings.MEDIA_ROOT / "tmp" / session_id
    os.makedirs(tmp_dir, exist_ok=True)

    file_path = tmp_dir / file.name

    sha256 = hashlib.sha256()

    with open(file_path, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)
            sha256.update(chunk)

    return {
        "file_path": str(file_path),
        "file_hash": sha256.hexdigest()
    }
