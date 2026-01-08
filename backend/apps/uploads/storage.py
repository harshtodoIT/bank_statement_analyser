import os
import hashlib
from django.conf import settings


def save_temp_file(file, session_id):
    """
    Saves file to media/tmp/<session_id>/ and returns file path and hash.
    Rejects duplicate uploads based on hash within the same session.
    """

    tmp_dir = settings.MEDIA_ROOT / "tmp" / session_id
    os.makedirs(tmp_dir, exist_ok=True)

    sha256 = hashlib.sha256()
    file_bytes = b""

    for chunk in file.chunks():
        sha256.update(chunk)
        file_bytes += chunk

    file_hash = sha256.hexdigest()
    file_path = tmp_dir / file.name

    # duplicate detection
    for existing_file in tmp_dir.iterdir():
        if existing_file.is_file():
            with open(existing_file, "rb") as f:
                existing_hash = hashlib.sha256(f.read()).hexdigest()
                if existing_hash == file_hash:
                    raise ValueError("Duplicate file upload detected.")

    with open(file_path, "wb") as destination:
        destination.write(file_bytes)

    return {
        "file_path": str(file_path),
        "file_hash": file_hash
    }
