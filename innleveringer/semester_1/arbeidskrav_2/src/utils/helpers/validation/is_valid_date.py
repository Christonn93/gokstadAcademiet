from datetime import datetime

def is_valid_date(date_str):
    """Validate a date string in YYYY-MM-DD format"""

    # Attempt to parse the date using datetime; catch invalid formats
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
