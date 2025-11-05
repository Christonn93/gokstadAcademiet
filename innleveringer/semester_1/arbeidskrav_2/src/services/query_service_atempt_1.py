from database.query_db import query_db

# My attempt on creating a class service. Did nto end up using this

class QueryService:
    def __init__(self):
        """Initialize the QueryService - no connection needed as query_db handles it"""
        pass

    # 1. Get all books published after a specific year
    def get_books_after_year(self, year=2000):
        query = "SELECT * FROM bok WHERE UtgittÅr > %s"
        return query_db(query, (year,), fetch=True)

    # 2. Get author names and book titles sorted alphabetically by author
    def get_books_sorted_by_author(self):
        query = "SELECT Forfatter, Tittel FROM bok ORDER BY Forfatter ASC"
        return query_db(query, fetch=True)

    # 3. Get all books with more than specified number of pages
    def get_books_by_page_count(self, min_pages=300):
        query = "SELECT * FROM bok WHERE AntallSider > %s"
        return query_db(query, (min_pages,), fetch=True)

    # 4. Add a new book to the 'bok' table
    def add_new_book(self, isbn, tittel, forfatter, utgitt_ar, antall_sider):
        query = """
                INSERT INTO bok (ISBN, Tittel, Forfatter, UtgittÅr, AntallSider)
                VALUES (%s, %s, %s, %s, %s) \
                """
        params = (isbn, tittel, forfatter, utgitt_ar, antall_sider)
        return query_db(query, params, fetch=False)

    # 5. Add a new borrower to the 'låner' table
    def add_new_borrower(self, navn, adresse):
        query = "INSERT INTO låner (Navn, Adresse) VALUES (%s, %s)"
        params = (navn, adresse)
        return query_db(query, params, fetch=False)

    # 6. Update address for a specific borrower
    def update_borrower_address(self, borrower_id, new_address):
        query = "UPDATE låner SET Adresse = %s WHERE LNr = %s"
        params = (new_address, borrower_id)
        return query_db(query, params, fetch=False)

    # 7. Get all loans with borrower names and book titles
    def get_loans_with_details(self):
        query = """
                SELECT u.*, l.Navn as LånerNavn, b.Tittel as BokTittel
                FROM utlån u
                         JOIN låner l ON u.LNr = l.LNr
                         JOIN bok b ON u.ISBN = b.ISBN \
                """
        return query_db(query, fetch=True)

    # 8. Get all books with count of copies
    def get_books_with_copy_count(self):
        query = """
                SELECT b.*, COUNT(e.EksNr) as AntallEksemplarer
                FROM bok b
                         LEFT JOIN eksemplar e ON b.ISBN = e.ISBN
                GROUP BY b.ISBN \
                """
        return query_db(query, fetch=True)

    # 9. Get loan count per borrower
    def get_loans_per_borrower(self):
        query = """
                SELECT l.Navn, COUNT(u.UtlånsNr) as AntallUtlån
                FROM låner l
                         LEFT JOIN utlån u ON l.LNr = u.LNr
                GROUP BY l.LNr, l.Navn \
                """
        return query_db(query, fetch=True)

    # 10. Get loan count per book
    def get_loans_per_book(self):
        query = """
                SELECT b.Tittel, COUNT(u.UtlånsNr) as AntallUtlån
                FROM bok b
                         LEFT JOIN utlån u ON b.ISBN = u.ISBN
                GROUP BY b.ISBN, b.Tittel \
                """
        return query_db(query, fetch=True)

    # 11. Get books that have never been borrowed
    def get_unborrowed_books(self):
        query = """
                SELECT b.*
                FROM bok b
                         LEFT JOIN utlån u ON b.ISBN = u.ISBN
                WHERE u.UtlånsNr IS NULL \
                """
        return query_db(query, fetch=True)

    # 12. Get author and count of loaned books per author
    def get_loans_per_author(self):
        query = """
                SELECT b.Forfatter, COUNT(u.UtlånsNr) as AntallUtlån
                FROM bok b
                         LEFT JOIN utlån u ON b.ISBN = u.ISBN
                GROUP BY b.Forfatter \
                """
        return query_db(query, fetch=True)

    # Bonus: Flexible book search method (combines multiple criteria)
    def search_books(self, year=None, search_param=None, min_pages=None):
        query = "SELECT * FROM bok WHERE 1=1"
        params = []

        if year:
            query += " AND UtgittÅr > %s"
            params.append(year)

        if search_param:
            query += " AND (Tittel LIKE %s OR Forfatter LIKE %s)"
            params.extend([f"%{search_param}%", f"%{search_param}%"])

        if min_pages:
            query += " AND AntallSider > %s"
            params.append(min_pages)

        return query_db(query, params, fetch=True)