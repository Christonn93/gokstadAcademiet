from database import query_db

class BookService:
    """Handles all book-related queries"""

    @staticmethod
    def get_books_after_year(year=2000):
        """1. Get all books published after specified year"""
        query = "SELECT * FROM bok WHERE UtgittÅr > %s"
        return query_db(query, (year,), fetch=True)

    @staticmethod
    def get_books_sorted_by_author():
        """2. Get author names and book titles sorted alphabetically by author"""
        query = "SELECT Forfatter, Tittel FROM bok ORDER BY Forfatter"
        return query_db(query, fetch=True)

    @staticmethod
    def get_books_by_page_count(min_pages=300):
        """3. Get all books with more than specified number of pages"""
        query = "SELECT * FROM bok WHERE AntallSider > %s"
        return query_db(query, (min_pages,), fetch=True)

    @staticmethod
    def add_new_book(isbn, tittel, forfatter, forlag, utgitt_ar, antall_sider):
        """4. Add a new book to the 'bok' table (checks for duplicate ISBN first)"""

        # Check if ISBN already exists
        check_query = "SELECT COUNT(*) AS count FROM bok WHERE ISBN = %s"
        result = query_db(check_query, (isbn,), fetch=True)

        if result and result[0]["count"] > 0:
            print(f"⚠️  A book with ISBN {isbn} already exists in the database.")
            return None

        # Proceed with insertion if not duplicate
        insert_query = """
                       INSERT INTO bok (ISBN, Tittel, Forfatter, Forlag, UtgittÅr, AntallSider)
                       VALUES (%s, %s, %s, %s, %s, %s) \
                       """
        params = (isbn, tittel, forfatter, forlag, utgitt_ar, antall_sider)

        try:
            query_db(insert_query, params, fetch=False)
            print("✅ Book added successfully.")
        except Exception as e:
            print(f"❌ Error adding book: {e}")

    @staticmethod
    def get_books_with_copy_count():
        """8. Get all books and number of copies per book"""
        query = """
                SELECT b.ISBN,
                       b.Tittel,
                       COUNT(e.EksNr) AS AntallEksemplarer
                FROM bok b
                         LEFT JOIN eksemplar e ON b.ISBN = e.ISBN
                GROUP BY b.ISBN, b.Tittel
                ORDER BY b.Tittel \
                """
        return query_db(query, fetch=True)

    @staticmethod
    def get_books_not_loaned():
        """11. Get all books that have not been loaned out"""
        query = """
            SELECT 
                b.ISBN, 
                b.Tittel, 
                b.Forfatter
            FROM bok b
            LEFT JOIN utlån u ON b.ISBN = u.ISBN
            WHERE u.UtlånsNr IS NULL
        """
        return query_db(query, fetch=True)

    @staticmethod
    def get_all_books():
        query = """SELECT * FROM bok"""
        return query_db(query, fetch=True)
