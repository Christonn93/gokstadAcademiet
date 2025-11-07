# 📚 Library Database System – README

## 🏢 Project Overview
The **ga_bibliotek** system is a database-driven application designed to support a small library’s operations. It enables users to borrow books and allows the library to manage records of books, copies, borrowers, and loan transactions.

---

## 📋 Table of Contents
- [Assignment Brief](#assignment-brief)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Folder Structure](#folder-structure)
- [Program Logic](#program-logic)
- [Functional Mapping](#functional-mapping)
- [Usage](#usage)
- [Acknowledgments](#acknowledgments)
- [Resources](#resources)
- [AI Documentation](#ai-documentation)
- [License](#license)
- [Contact](#contact)

---

## 📑 Assignment Brief

This project fulfills the requirements of the **Tema 2: Databasesystemer** assignment at Gokstad Akademiet. It is delivered as a fully functional program with clearly mapped code files for each task:

### 🧩 Task 1 – Database Creation
- [`create_database.sql`](src/database/sql/create_database.sql) – Creates the database.
- [`create_database_tables.sql`](src/database/sql/create_database_tables.sql) – Defines tables.
- [`seed_database.sql`](src/database/sql/seed_database.sql) – Inserts example data.

### 🧩 Task 2 – Database Design Explanation
- [`README_main.MD`](src/database/README_main.MD) – Explains database structure, keys, and constraints.

### 🧩 Task 3 – SQL Queries
- [`queries.sql`](src/database/sql/queries.sql) – Contains all required SQL queries.

### 🧩 Task 4 – Python Integration
- Python modules in `src/services/` and `src/database/` implement the required functionality.

---

## 🛠️ Installation

### Prerequisites
- Python 3.12+
- Docker & Docker Compose
- MySQL Connector for Python

### Setup Steps

1. **Install Python 3.12**  
   Download from [python.org](https://www.python.org) and verify:
   ```bash
   python --version
   ```

2. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd arbeidskrav_2
   ```

3. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   ```

   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

6. **Start MySQL container**
   ```bash
   docker run -p 3306:3306 --name ga-mysql-2025 -v ga-vol-2025:/var/lib/mysql -d --restart unless-stopped yngvemag/ga-mysql-db
   ```

---

## 🏃 Running the Project

### Option 1: Run via Python
```bash
  cd src
  python main.py
```

### Option 2: Run via Docker Compose
```bash
docker compose -f docker/compose.yml up -d
```

Access [phpMyAdmin](http://localhost:8080/index.php) to view your database.

> ⚠️ Note: The Docker setup is not fully operational yet.

---

## 📂 Folder Structure

```plaintext
arbeidskrav_2/
├── .docs/              ← AI-generated documentation and design notes
├── docker/             ← Docker setup files
├── init.d/             ← SQL initialization scripts
├── src/                ← Main application code
│   ├── config/         ← Configuration settings
│   ├── constants/      ← Constant values and SQL paths
│   ├── database/       ← Database logic and SQL scripts
│   ├── interface/      ← Command-line interface
│   ├── services/       ← Business logic for books, loans, etc.
│   └── utils/          ← Utility modules (handlers, helpers)
├── .env.example        ← Environment variable template
├── .gitignore          ← Git ignore rules
├── main.py             ← Application entry point
├── README.MD           ← This file
└── requirements.txt    ← Python dependencies
```

---

## 💽 Program Logic

```plaintext
[ main.py ] ──────── CLI interface
     │
     ▼
[ services/* ] ───── Business logic
     │
     ▼
[ utils/* ] ───────── Input, error, formatting, validation
     │
     ▼
[ database/* ] ────── SQL execution and connection handling
```

---

## 🧩 Functional Mapping

| Assignment Task       | File Location              | Function(s)                             |
|-----------------------|----------------------------|-----------------------------------------|
| Connect to database   | `database/connect_db.py`   | `connect_to_database()`                 |
| Fetch all books       | `services/book_service.py` | `get_all_books()`                       |
| Search books          | `services/book_service.py` | `search_books(keyword)`                 |
| Register new loan     | `services/loan_service.py` | `register_loan(lnr, isbn, eksnr, date)` |
| Return book           | `services/loan_service.py` | `return_book(utlansnr)`                 |
| Show borrower history | `services/loan_service.py` | `get_borrower_history(lnr)`             |

---

## 💻 Usage

### SQL Scripts
- Create schema: `src/database/sql/create_database.sql`
- Run queries: `src/database/sql/queries.sql`

### Python Modules
- Connect to DB: `connect_db.py`
- Book operations: `book_service.py`
- Loan operations: `loan_service.py`

---

## 🙏 Acknowledgments
- Gokstad Akademiet for the assignment framework  
- MySQL and Python communities for documentation  
- AI tools used for documentation and code suggestions: [AI Help](.docs/AI-Help)

---

## 📚 Resources
- [MySQL Docs](https://dev.mysql.com/doc/)
- [Python MySQL Connector](https://dev.mysql.com/doc/connector-python/en/)
- [Database Design Best Practices](https://www.guru99.com/database-design.html)
- [MySQL Connector Tutorial](https://www.mysqltutorial.org/python-mysql/getting-started-mysql-python-connector/)

---

## 🤖 AI Documentation

AI assistance was used for:
- Code structure and optimization
- SQL query validation
- Documentation generation

**Tools Used:**
- ChatGPT
- DeepSeek

---

## 📄 License
This project is licensed under the MIT License.  
See the `LICENSE` file for details.

---

## 📞 Contact

**Christopher Tønnesland**  
🌐 [ChrisDev.no](https://www.chrisDev.no)

---

_Last updated: 2025-10-27_
