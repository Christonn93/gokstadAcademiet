from utils.handlers.logger.get_logger import logger

def handle_db_error(err):
    """Handle and log the specific database error and notify the user"""
    logger.error(f"Database error: {err}")
    print("A database error occurred. Please check the logs for more details.")