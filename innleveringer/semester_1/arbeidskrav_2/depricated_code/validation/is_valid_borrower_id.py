import re

def is_valid_borrower_id(borrower_id):
    """Validate a borrower ID (pattern: LNr followed by digits)"""

    # Check borrower ID format with a regular expression
    return re.match(r"^LNr\d+$", borrower_id) is not None
