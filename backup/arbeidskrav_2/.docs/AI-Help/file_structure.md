Prompt:

> Lets talk about how I can structure my school assignment. I do not want any syntax, I just want to have some ideas on how to structure the project. I'm fresh into working with python. Its important that the structure is good and makes it easy to
> navigate for the teacher that will evaluate my project

Response:

Perfect — this is a classic database-driven Python assignment, and the grading criteria make it clear that **structure, clarity, and readability** count for as much as correctness. So, you want your teacher to open your project and instantly
understand where to look for what.

Here’s how you can structure it, without any syntax or code — just the logic of organization and workflow:

---

### 🧱 1. Folder and File Structure

A clean folder layout communicates thoughtfulness. Something like:

```
arbeidskrav_2/
│
├── sql/
│   ├── create_database.sql      ← Oppgave 1: all CREATE TABLE + INSERTs
│   ├── queries.sql              ← Oppgave 3: all SELECT/UPDATE queries
│
├── python/
│   ├── main.py                  ← Runs your functions / main program flow
│   ├── db_connection.py         ← Handles MySQL connection (Oppgave 4A)
│   ├── book_functions.py        ← vis_alle_boker(), sok_bok() (Oppgave 4B–C)
│   ├── loan_functions.py        ← registrer_utlan(), lever_bok(), vis_lanerhistorikk()
│
├── README.md                    ← Oppgave 2: explanation of database and relationships
└── requirements.txt             ← Lists mysql-connector-python and other dependencies
```

This makes the project feel modular, like a small real-world application rather than one long file.

---

### 🧩 2. Logical Structure

Each file has a single responsibility:

- **`create_database.sql`**: Sets up the schema and inserts sample data. Keep it cleanly commented — `-- Create table 'bok'`.
- **`queries.sql`**: Contains all 12 queries with headers like `-- Query 1: Books after year 2000`.
- **`db_connection.py`**: Contains only the logic to connect to `ga_bibliotek`. Import this file everywhere else instead of rewriting the connection.
- **`book_functions.py`**: Functions dealing with the book table (fetch, search).
- **`loan_functions.py`**: Functions dealing with loan registration and returns.
- **`main.py`**: Your "entry point." It could simply call the functions in order or provide a simple menu interface.

That separation shows an understanding of _Single Responsibility Principle_ — something teachers love to see, even in beginner projects.

---

### 📘 3. README Structure (Oppgave 2)

Since this counts for 25%, write it clearly and logically:

1. **Introduction** – What the database models (a small library system).
2. **ER model overview** – Briefly describe relationships between the four tables.
3. **Table descriptions** – Each table, its columns, data types, constraints.
4. **Keys and relationships** – Primary and foreign keys, how they connect.
5. **Constraints explanation** – Why they exist (e.g., `NOT NULL`, `AUTO_INCREMENT`).
6. **Design reasoning** – Explain why this structure ensures data integrity and prevents duplication.

If you include a **diagram** (like from draw.io), it adds a professional polish.

---

### ⚙️ 4. Python Code Flow (Conceptually)

When the teacher runs your `main.py`, the flow should feel intuitive:

1. **Connect to the database**
2. **Display menu / call functions**

   - Show all books
   - Search for a book
   - Register new loan
   - Return book
   - View loan history

Add clear print statements and formatted output — it doesn’t need to be fancy, just clean.

---

### 🧭 5. Comments and Naming

Since you’re new to Python, this is where you can stand out:

- Use **meaningful variable names** (`loan_id`, `isbn_number`, `connection`).
- Comment short explanations above functions: “Connects to MySQL and returns a connection object.” “Registers a new loan if book copy is available.”

That makes your teacher’s job easy — they won’t need to guess what your code does.

---

### 🧩 6. Final Touches

- Include a `requirements.txt` (one line: `mysql-connector-python`).
- Use consistent indentation and blank lines between functions.
- At the end of `main.py`, add a comment: “# End of program — all database connections are closed properly.”
- Test your `.zip` before submitting: open it fresh and make sure all files run without missing paths.

---

Would you like me to outline an **example project structure tree with descriptions for each file**, as it would appear in your zip file? That could help you map it 1:1 before you start coding.
