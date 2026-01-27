import os
import shutil
import logging

logger = logging.getLogger(__name__)


def delete_folder(folder_path):
    """
    Deletes a folder and all its contents safely.
    Used for TEMPORARY privacy mode cleanup.
    """
    try:
        if folder_path and os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            logger.info(f"Deleted folder: {folder_path}")
    except Exception as e:
        logger.error(f"Failed to delete folder {folder_path}: {str(e)}")
