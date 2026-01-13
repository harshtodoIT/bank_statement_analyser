from apps.reporting.services import generate_report


def get_export_data(result):
    """
    Single source of truth for all exports
    """
    return generate_report(result)