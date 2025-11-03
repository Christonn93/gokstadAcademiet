from database import query_db

class LoanService:
    """Handles all loan-related queries"""

    @staticmethod
    def get_all_loans_with_details():
        """7. Get all loans with borrower full names and book titles"""
        query = """
            SELECT 
                u.UtlånsNr,
                CONCAT(l.Fornavn, ' ', l.Etternavn) AS LånerNavn,
                b.Tittel AS BokTittel,
                u.Utlånsdato,
                u.Utlånsdato,
                u.Levert
            FROM utlån u
            JOIN låner l ON u.LNr = l.LNr
            JOIN bok b ON u.ISBN = b.ISBN
            ORDER BY u.Utlånsdato DESC
        """
        return query_db(query, fetch=True)

    @staticmethod
    def get_loan_count_per_borrower():
        """9. Get loan count per borrower with full names"""
        query = """
            SELECT 
                CONCAT(l.Fornavn, ' ', l.Etternavn) AS Navn, 
                COUNT(u.UtlånsNr) AS AntallUtlån
            FROM låner l
            LEFT JOIN utlån u ON l.LNr = u.LNr
            GROUP BY l.LNr, l.Fornavn, l.Etternavn
            ORDER BY AntallUtlån DESC
        """
        return query_db(query, fetch=True)

    @staticmethod
    def get_loan_count_per_book():
        """10. Get number of loans per book"""
        query = """
            SELECT 
                b.ISBN,
                b.Tittel,
                COUNT(u.UtlånsNr) AS AntallUtlån
            FROM bok b
            LEFT JOIN utlån u ON b.ISBN = u.ISBN
            GROUP BY b.ISBN, b.Tittel
            ORDER BY AntallUtlån DESC
        """
        return query_db(query, fetch=True)

    @staticmethod
    def get_loaned_books_per_author():
        """12. Get author and number of loaned books per author"""
        query = """
            SELECT 
                b.Forfatter,
                COUNT(u.UtlånsNr) AS AntallUtlån
            FROM bok b
            JOIN utlån u ON b.ISBN = u.ISBN
            GROUP BY b.Forfatter
            ORDER BY AntallUtlån DESC
        """
        return query_db(query, fetch=True)

    @staticmethod
    def register_loan(lnr, isbn, eksnr, utlaansdato):
        """Register a new loan"""
        query = """
            INSERT INTO utlån (LNr, ISBN, EksNr, Utlånsdato, Levert)
            VALUES (%s, %s, %s, %s, 0)
        """
        params = (lnr, isbn, eksnr, utlaansdato)
        return query_db(query, params, fetch=False)
