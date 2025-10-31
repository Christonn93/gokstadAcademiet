from .logging_handler import get_logger

logger = get_logger(__name__)

def handle_db_error(err):
    logger.error(f"Database error: {err}")
    print("A database error occurred. Please check the logs for more details.")

def handle_error(err):
    logger.error(f"An unexpected error occurred: {err}")
    print("An unexpected error occurred. Please check the logs for more details.")