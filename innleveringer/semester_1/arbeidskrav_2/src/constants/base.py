import os

BASE_DIR = os.path.dirname(__file__)
SQL_DIR = os.path.join(BASE_DIR, '..', 'database', 'sql')

for file in os.listdir(SQL_DIR):
 print(f"Available sql files: {file}")