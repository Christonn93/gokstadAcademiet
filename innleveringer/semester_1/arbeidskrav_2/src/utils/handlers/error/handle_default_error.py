from utils.handlers.logger.get_logger import logger

def handle_default_error(err):
    """Handle and log unexpected errors that occur outside database operations"""
    logger.error(f"An unexpected error occurred: {err}")
    print("An unexpected error occurred. Please check the logs for more details.")
