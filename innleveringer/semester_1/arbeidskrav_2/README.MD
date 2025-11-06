# Library Database System - README

## 🏢 Project Overview
The **ga_bibliotek** database system is designed to support a small library's operations, allowing users to borrow books while maintaining comprehensive records of books, copies, borrowers, and loan transactions.

---

## 📋 Table of Contents
- [Assignment brief](#Assignment brief)
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

## Assignment brief

I wanted to deliver the assignment as a fully working program. To point teachers to code that have relation with assignment task, I have decided to list codefiles here for easy navigation

### Task 1 - Opprettelse av Databasen og Tabellene

1. [Database script](python/db/sql/create_database.sql)
2. [Database tables](python/db/sql/create_database_tables.sql)
3. [Database seeding](python/db/sql/seed_database.sql)

### Task 2 - Forståelse og forklaring av database design

[Database Readme](./.docs/database/README.md)

### Task 3 

[Queries](python/db/sql/queries.sql)

### Task 4 - Python og MySQL Integration 

---

## 🛠️ Installation

### Prerequisites
- Docker and Docker Compose
- Python 3.12+
- MySQL Connector for Python

### Setup Steps

#### 1. Install Python 3.12

**Windows & macOS**
- Download Python 3.12 from the official Python website.
- Run the installer (ensure "Add Python to PATH" is checked).
- Check installation:

```bash
  python --version
```

#### 2. Clone and enter the repository

```bash
   git clone <repository-url>
   cd innleveringer/semester_1/arbeidskrav_2
```

#### 3. Create a virtual environment

```bash
    python -m venv .venv
```

#### 4. Activate the environment

**Windows:**
```bash
    .venv\Scripts\activate
```

**macOS/Linux:**
```bash
    source .venv/bin/activate
```

#### 5. **Install Python dependencies**

```bash
  python.exe -m pip install --upgrade pip
```


```bash
   pip install -r requirements.txt
```

#### 6. **Configure Environment Variables**
   - Copy `.env.example` to `.env`
   - Update the values in `.env` as needed


#### 7. **Start Database Services**
   ```bash
    docker run -p 3306:3306 --name ga-mysql-2025 -v ga-vol-2025:/var/lib/mysql -d --restart unless-stopped yngvemag/ga-mysql-db
   ```

---

## 🏃 Run the project

1. Run Python scripts
    ```bash
        python ./python/main.py
    ```

> Can also run it with the included docker. Then the default docker needs to be closed

Start docker container
    ```bash
        docker compose -f ./docker/compose.yml up -d
    ```
> You can now navigate to [phpMyadmin](http://localhost:8080/index.php) in the browser, input the password and username to view a local version of your database

NOTE: Not fully operative!!! 

---



## 📂 Folder Structure
```
arbeidskrav_2/
├── .docs/                      ← Contains project documentation, including AI-generated suggestions and images.
├── docker/                     ← Contains Docker-related files for containerizing the application.
│   ├── Dockerfile              ← Defines the Docker image for the Python application.
│   └── compose.yml             ← Defines the Docker Compose services for the application and database.
├── init.d/                     ← Contains initialization scripts for the database.
│   └── 10-init.sql             ← SQL script for initial database setup.
├── src/                        ← Contains the main source code for the Python application.
│   ├── config/                 ← Contains configuration files for the application.
│   │   └── database.py         ← Contains database configuration settings.
│   ├── constants/              ← Contains constant values used throughout the application.
│   │   ├── base.py             ← Contains base constants.
│   │   └── sql_files.py        ← Contains paths to SQL files.
│   ├── database/               ← Contains modules for interacting with the database.
│   │   ├── sql/                ← Contains SQL scripts for database operations.
│   │   │   ├── create_database.sql       ← SQL script for creating the database.
│   │   │   ├── create_database_tables.sql← SQL script for creating database tables.
│   │   │   ├── queries.sql               ← Contains various SQL queries.
│   │   │   └── seed_database.sql         ← SQL script for seeding the database with initial data.
│   │   ├── connect_db.py       ← Module for connecting to the database.
│   │   ├── create_db.py        ← Module for creating the database.
│   │   ├── create_db_tables.py ← Module for creating database tables.
│   │   ├── disconnect_db.py    ← Module for disconnecting from the database.
│   │   ├── drop_db.py          ← Module for dropping the database.
│   │   ├── query_db.py         ← Module for querying the database.
│   │   └── seed_db.py          ← Module for seeding the database.
│   ├── interface/              ← Contains the user interface for the application.
│   │   └── program.py          ← The main command-line interface for the application.
│   ├── services/               ← Contains the business logic for the application.
│   │   ├── book_service.py     ← Service for managing books.
│   │   ├── borrower_service.py ← Service for managing borrowers.
│   │   ├── database_service.py ← Service for managing the database.
│   │   └── loan_service.py     ← Service for managing loans.
│   └── utils/                  ← Contains utility functions and helper modules.
│       ├── handlers/           ← Contains handlers for various tasks.
│       ├── helpers/            ← Contains helper functions.
│       └── __init__.py         ← Initializes the utils package.
├── .env.example                ← Example environment file.
├── .gitignore                  ← Specifies files and directories to be ignored by Git.
├── main.py                     ← The main entry point for the application.
├── README.MD                   ← This file.
└── requirements.txt            ← Contains the Python dependencies for the project.
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
- [Getting Started with MySQL Connector/Python](https://www.mysqltutorial.org/python-mysql/getting-started-mysql-python-connector/)

---

## 🤖 AI Documentation
This project utilized AI assistance for:
- Code structure optimization
- Documentation template creation
- SQL query validation

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