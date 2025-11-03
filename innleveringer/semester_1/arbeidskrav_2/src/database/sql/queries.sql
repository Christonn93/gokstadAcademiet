# -------------------------
#  This file contains SQL queries for the library database.
#  Queries include selects, inserts, updates, and aggregations for books, borrowers, and loans.
#  All queries are organized for easy reference and use in Python scripts.
#
#  I folowed the same comment setup as I got suggested by AI previus
# -------------------------

# -------------------------
# 1. All books published after 2000
# -------------------------
QUERY_BOOKS_AFTER_2000 = """
SELECT *
FROM books
WHERE published_year > 2000 -- only books published after 2000
ORDER BY published_year DESC; -- newest books first
"""

# -------------------------
# 2. Author names and book titles sorted alphabetically by author
# -------------------------
QUERY_BOOKS_BY_AUTHOR = """
SELECT author, title
FROM books
ORDER BY author, title; -- sort by author, then by title
"""

# -------------------------
# 3. Books with more than 300 pages
# -------------------------
QUERY_BOOKS_OVER_300_PAGES = """
SELECT title, author, number_of_pages
FROM books
WHERE number_of_pages > 300 -- only books longer than 300 pages
ORDER BY number_of_pages DESC; -- longest books first
"""

# -------------------------
# 4. Insert a new book
# -------------------------
QUERY_INSERT_BOOK = """
INSERT INTO books (
    isbn, title, author, publisher, published_year, number_of_pages, genre
) VALUES (%s, %s, %s, %s, %s, %s, %s); -- placeholders for book data
"""

# Example data for insertion
NEW_BOOK_DATA = ('978-1501175466', 'The Shining', 'Stephen King', 'Doubleday', 1977, 447, 'Horror')

# -------------------------
# 5. Insert a new borrower
# -------------------------
QUERY_INSERT_BORROWER = """
INSERT INTO borrower (
    loan_number, first_name, last_name, address, street_number, city, postal_code
) VALUES (%s, %s, %s, %s, %s, %s, %s); -- placeholders for borrower data
"""

# Example borrower data
NEW_BORROWER_DATA = ('LN016', 'Kari', 'Nordmann', '888 Fjord Road', '888', 'Ålesund', '6008')

# -------------------------
# 6. Update borrower address
# -------------------------
QUERY_UPDATE_BORROWER_ADDRESS = """
UPDATE borrower
SET address = %s,
    street_number = %s,
    city = %s,
    postal_code = %s
WHERE loan_number = %s; -- update by loan_number
"""

# Example update data
UPDATE_ADDRESS_DATA = ('999 Mountain View', '999', 'Bergen', '5008', 'LN002')

# -------------------------
# 7. All loans with borrower names and book titles
# -------------------------
QUERY_LOANS_WITH_DETAILS = """
SELECT
    l.loan_number,
    b.first_name,
    b.last_name,
    bk.title,
    l.loan_date,
    l.due_date,
    l.status
FROM loan l
JOIN borrower b ON l.borrower_loan_number = b.loan_number -- join to get borrower names
JOIN books bk ON l.isbn = bk.isbn -- join to get book titles
ORDER BY l.loan_date DESC; -- newest loans first
"""

# -------------------------
# 8. Books and their copy counts
# -------------------------
QUERY_BOOKS_COPY_COUNTS = """
SELECT
    b.isbn,
    b.title,
    b.author,
    COUNT(c.example_number) AS copy_count -- count how many copies exist
FROM books b
LEFT JOIN copy c ON b.isbn = c.isbn
GROUP BY b.isbn, b.title, b.author
ORDER BY copy_count DESC; -- most copies first
"""

# -------------------------
# 9. Loan count per borrower
# -------------------------
QUERY_LOANS_PER_BORROWER = """
SELECT
    b.loan_number,
    b.first_name,
    b.last_name,
    COUNT(l.loan_number) AS loan_count -- number of loans per borrower
FROM borrower b
LEFT JOIN loan l ON b.loan_number = l.borrower_loan_number
GROUP BY b.loan_number, b.first_name, b.last_name
ORDER BY loan_count DESC; -- borrowers with most loans first
"""

# -------------------------
# 10. Loan count per book
# -------------------------
QUERY_LOANS_PER_BOOK = """
SELECT
    bk.isbn,
    bk.title,
    bk.author,
    COUNT(l.loan_number) AS loan_count -- number of times book was borrowed
FROM books bk
LEFT JOIN loan l ON bk.isbn = l.isbn
GROUP BY bk.isbn, bk.title, bk.author
ORDER BY loan_count DESC; -- most borrowed books first
"""

# -------------------------
# 11. Books never borrowed
# -------------------------
QUERY_UNBORROWED_BOOKS = """
SELECT
    bk.isbn,
    bk.title,
    bk.author
FROM books bk
LEFT JOIN loan l ON bk.isbn = l.isbn
WHERE l.loan_number IS NULL -- books with no loans
ORDER BY bk.title; -- sort alphabetically
"""

# -------------------------
# 12. Authors and their borrowed book counts
# -------------------------
QUERY_AUTHOR_LOAN_COUNTS = """
SELECT
    bk.author,
    COUNT(l.loan_number) AS books_borrowed -- total loans per author
FROM books bk
LEFT JOIN loan l ON bk.isbn = l.isbn
WHERE l.loan_number IS NOT NULL
GROUP BY bk.author
ORDER BY books_borrowed DESC; -- authors with most borrowed books first
"""

# -------------------------
# Dictionary of all queries for easy access
# -------------------------
ALL_QUERIES = {
    'books_after_2000': QUERY_BOOKS_AFTER_2000,
    'books_by_author': QUERY_BOOKS_BY_AUTHOR,
    'books_over_300_pages': QUERY_BOOKS_OVER_300_PAGES,
    'insert_book': QUERY_INSERT_BOOK,
    'insert_borrower': QUERY_INSERT_BORROWER,
    'update_borrower_address': QUERY_UPDATE_BORROWER_ADDRESS,
    'loans_with_details': QUERY_LOANS_WITH_DETAILS,
    'books_copy_counts': QUERY_BOOKS_COPY_COUNTS,
    'loans_per_borrower': QUERY_LOANS_PER_BORROWER,
    'loans_per_book': QUERY_LOANS_PER_BOOK,
    'unborrowed_books': QUERY_UNBORROWED_BOOKS,
    'author_loan_counts': QUERY_AUTHOR_LOAN_COUNTS
}
