import sys
import os

project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from app.menu import display_menu, get_user_choice
from app.controller import handle_user_choice
from db.db_connection import create_connection, close_connection

def main():
    db_conn = create_connection()
    running = True

    while running:
        display_menu()
        choice = get_user_choice()
        if choice:
            running = handle_user_choice(choice, db_conn)

    close_connection(db_conn)

if __name__ == "__main__":
    main()
