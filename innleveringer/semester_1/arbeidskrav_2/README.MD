# Library Database System - README

## 🏢 Project Overview
The **ga_bibliotek** database system is designed to support a small library's operations, allowing users to borrow books while maintaining comprehensive records of books, copies, borrowers, and loan transactions.

---

## 📋 Table of Contents
- [Database Design](#database-design)
- [Installation](#installation)
- [Folder Structure](#folder-structure)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)
- [Resources](#resources)
- [AI Documentation](#ai-documentation)

---

### 📊 Database Structure

[Read about the database structure here](./.docs/other/Notes.md)

---

## 🛠️ Installation

### Prerequisites
- Docker and Docker Compose
- Python 3.12+
- MySQL Connector for Python

### Setup Steps
1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd innleveringer/semester_1/arbeidskrav_2
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   - Copy `.env.example` to `.env`
   - Update the values in `.env` as needed

4. **Start Database Services**
   ```bash
   docker compose -f ./docker/compose.yml up -d
   ```

---

## 🏃 Run the project

1. Start docker container
    ```bash
        docker compose -f ./docker/compose.yml up -d
    ```
> You can now navigate to [phpMyadmin](http://localhost:8080/index.php) in the browser, input the password and username to view a local version of your database

2. Run Python scripts
    ```bash
        python ./python/main.py
    ```
---

## 📂 Folder Structure
```
arbeidskrav_2/
├── .docs/
│   ├── AI-Help/                    ← Documentation of AI-assisted suggestions, notes, or experiments
│   ├── images/                     ← Screenshots, diagrams, or visuals used in the documentation or README
│   └── other/                      ← Any additional reference materials or supporting documents
│
├── docker/
│   ├── Dockerfile                  ← Defines container environment for running the Python app
│   └── compose.yml                 ← Docker Compose setup for orchestrating services (e.g., app + database)
│
├── init.d/
│   └── 10-init.sql                 ← Initial SQL setup script for seeding or bootstrapping the database
│
├── sql/
│   ├── create_database.sql         ← Defines schema, tables, and constraints for the main database
│   └── queries.sql                 ← Reusable SQL queries for debugging or manual database operations
│
├── python/
│   ├── app/
│   │   ├── menu.py                 ← Command-line interface or text-based menu system for user navigation
│   │   └── controller.py           ← Connects menu actions to the correct service logic (acts as router)
│   │
│   ├── db/
│   │   ├── db_config.py            ← Configuration for database connections
│   │   ├── db_connection.py        ← Handles database connections (create_connection, close_connection)
│   │   └── schema.py               ← Python-side representation of database structure and models
│   │
│   ├── services/
│   │   ├── book_service.py         ← Business logic for managing books (CRUD, availability checks)
│   │   └── loan_service.py         ← Business logic for managing loans, due dates, and returns
│   │
│   ├── utils/
│   │   ├── handlers/
│   │   │   ├── db_handler.py       ← Wraps DB operations with retry logic and transaction management
│   │   │   ├── input_handler.py    ← Validates and sanitizes user input before passing to services
│   │   │   └── error_handler.py    ← Centralized logic for catching and formatting application errors
    │   │
│   │   └── helpers/
│   │       ├── formatters.py       ← Handles output formatting (e.g., table prints, reports, messages)
│   │       ├── validators.py       ← Input validation utilities for type checking and business rules
│   │       └── converters.py       ← Data conversion helpers (string↔bool, int↔str, date parsing, etc.)
│   │
│   └── main.py                     ← Main entry point; initializes app, loads config, runs main loop
│
├── .env                            ← Environment variables for local development (e.g., DB_URL)
├── .env.example                    ← Example template showing required .env keys and formats
├── requirements.txt                ← Python dependencies required to run the application
└── README.MD                       ← Project overview, setup guide, and usage instructions

```
---

## 💽 Program logics

```
[ main.py ] ──────── user interface
     │
     ▼
[ book_functions.py / loan_functions.py ] ─── business rules
     │
     ▼
[ utils.handlers ] ─── workflow management (errors, input)
     │
     ▼
[ utils.helpers ] ─── stateless utilities (validation, formatting)
     │
     ▼
[ lib.db ] ─── infrastructure (connection, queries)
```

---

## 🧩 Functional Mapping

| Assignment Task              | Implemented in                 | Core Function(s)                            |
|------------------------------|--------------------------------|---------------------------------------------|
| Connect to database          | `db/db_connection.py`          | `create_connection()`, `close_connection()` |
| Fetch all books              | `services/book_service.py`     | `get_all_books()`                           |
| Search books by title/author | `services/book_service.py`     | `search_books(keyword)`                     |
| Register new loan            | `services/loan_service.py`     | `register_loan(lnr, isbn, eksnr, date)`     |
| Return book                  | `services/loan_service.py`     | `return_book(utlansnr)`                     |
| Show borrower history        | `services/loan_service.py`     | `get_borrower_history(lnr)`                 |


---

## 🐛 Problems

During this assignment and how I have structured my GitHub repo to collect and contain all school related work in one repository I have been struggling with paths
All problems I have had during this Assignment is listed [here](./.docs/other/Problemer.md)

---

## 💻 Usage

### Running SQL Scripts
- Database schema creation: `sql/create_database.sql`
- Sample queries: `sql/queries.sql`

### Python Integration
The Python modules in the `python/` directory provide functions to:
- Connect to the database (`db_connection.py`)
- Manage book data (`book_functions.py`)
- Handle loan operations (`loan_functions.py`)

---

## 🙏 Acknowledgments
- Gokstad Akademiet for providing the assignment requirements
- MySQL and Python communities for excellent documentation
- Contributors and reviewers of this project
- Some AI help have been used, documentations for this can be found [here](./.docs/AI-Help)

---

## 📚 Resources
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [Python MySQL Connector Documentation](https://dev.mysql.com/doc/connector-python/en/)
- [Database Design Best Practices](https://www.guru99.com/database-design.html)

---

## 🤖 AI Documentation
This project utilized AI assistance for:
- Code structure optimization
- Documentation template creation
- SQL query validation
- Python function development

**AI Tools Used:**
- ChatGPT
- DeepSeek

**AI Contribution Areas:**
- Database schema design review
- SQL query optimization suggestions
- Python code structure recommendations
- Documentation template generation

---

## 📄 License
This project is licensed under the MIT License.  
See the LICENSE file for details.

---

## 📞 Contact
**Christopher Tønnesland**   
🌐 Website: [ChrisDev](https://www.chrisDev.no)

---

*Last updated: 2025-10-27*
```
