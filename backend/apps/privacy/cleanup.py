import os
import shutil
import logging

logger = logging.getLogger(__name__)


def delete_file(file_path):
    """
    Deletes a single file safely.
    """
    try:
        if file_path and os.path.exists(file_path):
            os.remove(file_path)
            logger.info(f"Deleted file: {file_path}")
    except Exception as e:
        logger.error(f"Failed to delete file {file_path}: {str(e)}")


def delete_folder(folder_path):
    """
    Deletes a folder and all its contents.
    """
    try:
        if folder_path and os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            logger.info(f"Deleted folder: {folder_path}")
    except Exception as e:
        logger.error(f"Failed to delete folder {folder_path}: {str(e)}")
