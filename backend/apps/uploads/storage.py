import os
import hashlib
from django.conf import settings
from pathlib import Path


def save_temp_file(file, session_id):
    """
    Saves file to media/tmp/<session_id>/.
    Allows re-uploads by overwriting previous temp file.
    """

    tmp_dir = Path(settings.MEDIA_ROOT) / "tmp" / session_id
    os.makedirs(tmp_dir, exist_ok=True)

    sha256 = hashlib.sha256()
    file_bytes = b""

    for chunk in file.chunks():
        sha256.update(chunk)
        file_bytes += chunk

    file_hash = sha256.hexdigest()

    # :fire: ALWAYS overwrite temp file
    file_path = tmp_dir / file.name

    with open(file_path, "wb") as destination:
        destination.write(file_bytes)

    return {
        "file_path": str(file_path),
        "file_hash": file_hash,
    }