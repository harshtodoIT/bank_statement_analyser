ALLOWED_EXTENSIONS = {'.pdf', '.csv', '.xls', '.xlsx'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB


def validate_file(file):
    """
    Validates uploaded file for presence, type, and size.
    Raises ValueError with clear message on failure.
    """

    if not file:
        raise ValueError("No file uploaded.")

    filename = file.name.lower()

    if not any(filename.endswith(ext) for ext in ALLOWED_EXTENSIONS):
        raise ValueError("Unsupported file type. Allowed: PDF, CSV, Excel.")

    if file.size > MAX_FILE_SIZE:
        raise ValueError("File size exceeds 10 MB limit.")

    return True
