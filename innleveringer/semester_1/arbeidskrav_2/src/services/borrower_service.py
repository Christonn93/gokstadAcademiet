from database import query_db

class BorrowerService:
    """Handles all borrower-related queries"""

    @staticmethod
    def add_new_borrower(fornavn, etternavn, adresse):
        """5. Add a new borrower with separate first and last names"""
        query = "INSERT INTO låner (Fornavn, Etternavn, Adresse) VALUES (%s, %s, %s)"
        params = (fornavn, etternavn, adresse)
        return query_db(query, params, fetch=False)

    @staticmethod
    def update_borrower_address(borrower_id, new_address):
        """6. Update address for a specific borrower"""
        query = "UPDATE låner SET Adresse = %s WHERE LNr = %s"
        params = (new_address, borrower_id)
        return query_db(query, params, fetch=False)

    @staticmethod
    def get_borrower_full_name(borrower_id):
        """Get borrower's full name by ID"""
        query = "SELECT CONCAT(Fornavn, ' ', Etternavn) AS FulltNavn FROM låner WHERE LNr = %s"
        return query_db(query, (borrower_id,), fetch=True)
