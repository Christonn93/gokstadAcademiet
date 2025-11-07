from interface.program import query_program
from services.database_service import database_service

def main_program():
    """The main program - orchestrates database setup and launches the application"""
    # Running database service
    database_service()

    # Launch the main user interface for querying the database
    query_program()

# Standard Python idiom to ensure code only runs when executed directly
if __name__ == '__main__':

    # Entry point when script is run directly
    main_program()
