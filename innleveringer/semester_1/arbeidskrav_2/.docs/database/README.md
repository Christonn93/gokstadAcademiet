# Database Structure

The database consists of four main tables that work together to manage library operations:

## Database Design

### Table Structures

#### 1. **bok** (Books Table)

Stores core information about books in the library collection.

| Column Name | Data Type    | Constraints           | Description                        |
| ----------- | ------------ | --------------------- | ---------------------------------- |
| ISBN        | VARCHAR(13)  | PRIMARY KEY, NOT NULL | International Standard Book Number |
| Tittel      | VARCHAR(255) | NOT NULL              | Book title                         |
| Forfatter   | VARCHAR(100) | NOT NULL              | Author name                        |
| Forlag      | VARCHAR(100) |                       | Publishing company                 |
| UtgittÅr    | INT          |                       | Publication year                   |
| AntallSider | INT          |                       | Number of pages                    |

#### 2. **exemplar** (Copies Table)

Tracks individual physical copies of each book.

| Column Name                              | Data Type   | Constraints           | Description         |
| ---------------------------------------- | ----------- | --------------------- | ------------------- |
| ISBN                                     | VARCHAR(13) | FOREIGN KEY, NOT NULL | References bok.ISBN |
| EksNr                                    | INT         | NOT NULL              | Copy number         |
| **Composite Primary Key:** (ISBN, EksNr) |             |                       |                     |

#### 3. **låner** (Borrowers Table)

Stores information about library members.

| Column Name | Data Type    | Constraints                 | Description        |
| ----------- | ------------ | --------------------------- | ------------------ |
| LNr         | INT          | PRIMARY KEY, AUTO_INCREMENT | Unique borrower ID |
| Fornavn     | VARCHAR(50)  | NOT NULL                    | First name         |
| Etternavn   | VARCHAR(50)  | NOT NULL                    | Last name          |
| Adresse     | VARCHAR(255) |                             | Physical address   |

#### 4. **utlån** (Loans Table)

Records all book lending transactions.

| Column Name | Data Type   | Constraints                 | Description                 |
| ----------- | ----------- | --------------------------- | --------------------------- |
| UtlånsNr    | INT         | PRIMARY KEY, AUTO_INCREMENT | Unique loan ID              |
| LNr         | INT         | FOREIGN KEY, NOT NULL       | References låner.LNr        |
| ISBN        | VARCHAR(13) | FOREIGN KEY, NOT NULL       | References bok.ISBN         |
| EksNr       | INT         | NOT NULL                    | Copy number                 |
| Utlånsdato  | DATE        | NOT NULL                    | Loan date                   |
| Levert      | TINYINT(1)  | CHECK (Levert IN (0,1))     | Return status (0=No, 1=Yes) |

### Primary Keys and Foreign Keys

#### Primary Keys:

- **bok**: ISBN
- **eksemplar**: Composite key (ISBN, EksNr)
- **låner**: LNr (Auto-increment)
- **utlån**: UtlånsNr (Auto-increment)

#### Foreign Keys:

- **eksemplar.ISBN** → bok.ISBN
- **utlån.LNr** → låner.LNr
- **utlån.(ISBN, EksNr)** → eksemplar.(ISBN, EksNr)

### Constraints and Data Integrity

#### Key Constraints:

- **NOT NULL**: Ensures essential fields like ISBN, titles, and names are always populated
- **PRIMARY KEY**: Guarantees uniqueness for entity identification
- **FOREIGN KEY**: Maintains referential integrity between related tables
- **CHECK CONSTRAINT**: In 'utlån' table, ensures 'Levert' only contains 0 or 1
- **AUTO_INCREMENT**: Automatically generates unique IDs for loans and borrowers

### Business Rules:
- Each book (bok) is uniquely identified by its ISBN
- Each physical copy (exemplar) is uniquely identified by (ISBN + EksNr)
- Loans (utlån) track which borrower (låner) borrowed which copy (eksemplar)
- Return status is enforced with CHECK constraint (0=not returned, 1=returned)

#### Relationship Diagram:

```
bok (1) ←→ (Many) eksemplar (1) ←→ (Many) utlån (Many) ←→ (1) låner
```
