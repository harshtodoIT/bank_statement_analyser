from .cleanup import delete_file
from .cleanup import delete_folder


def handle_post_processing_cleanup(
    uploaded_file_path=None,
    temp_folder_path=None,
    persist_data=False
):
    """
    Controls data cleanup after processing is complete.

    persist_data = False → delete everything
    persist_data = True  → keep minimal metadata only
    """

    # Default behavior: privacy-first
    if not persist_data:
        if uploaded_file_path:
            delete_file(uploaded_file_path)

        if temp_folder_path:
            delete_folder(temp_folder_path)

    else:
        if uploaded_file_path:
            delete_file(uploaded_file_path)
