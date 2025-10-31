import re
from datetime import datetime

def is_valid_isbn(isbn):
    """Validates a 10- or 13-digit ISBN."""
    isbn = isbn.replace("-", "").replace(" ", "").upper()
    if len(isbn) == 10 and isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == 'X'):
        return True
    if len(isbn) == 13 and isbn.isdigit():
        return True
    return False

def is_valid_date(date_str):
    """Validates a date string in YYYY-MM-DD format."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def is_valid_borrower_id(borrower_id):
    """Validates a borrower ID (e.g., LNr123)."""
    return re.match(r"^LNr\d+$", borrower_id) is not None
