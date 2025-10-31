import os
from dotenv import load_dotenv
from src.utils.handlers.error_handler import handle_env_error

def load_environment():
    """Load environment variables safely"""

    try:
        # Attempt to load environment variables from .env file
        if not load_dotenv():
            raise EnvironmentError(".env file not found or could not be loaded")

        # Define required environment variables that must exist
        required_vars = ["DB_HOST", "DB_USER", "DB_PASSWORD", "DB_NAME"]

        # Verify that each required variable is present in the environment
        for var in required_vars:
            if not os.getenv(var):
                raise EnvironmentError(f"Missing required environment variable: {var}")

    # Handle and log environment configuration errors
    except EnvironmentError as e:
        handle_env_error(e)
        exit(1)
