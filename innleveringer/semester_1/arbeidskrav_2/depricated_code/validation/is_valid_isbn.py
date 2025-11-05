def is_valid_isbn(isbn):
    """Validate a 10- or 13-digit ISBN"""

    # Remove hyphens and spaces, convert to uppercase for consistency
    isbn = isbn.replace("-", "").replace(" ", "").upper()

    # Validate ISBN-10 format (last digit may be 'X')
    if len(isbn) == 10 and isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == 'X'):
        return True

    # Validate ISBN-13 format (all digits)
    if len(isbn) == 13 and isbn.isdigit():
        return True

    # Return False if neither format matches
    return False