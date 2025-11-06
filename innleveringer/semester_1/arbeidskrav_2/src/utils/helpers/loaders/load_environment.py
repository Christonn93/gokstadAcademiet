import os
from dotenv import load_dotenv

def load_environment():
    """Load environment variables safely."""
    try:
        # Load variables from .env file
        if not load_dotenv():
            raise EnvironmentError("⚠️ .env file not found or could not be loaded.")

        # Required environment variables
        required_vars = ["DB_HOST", "DB_USER", "DB_PASSWORD", "DB_NAME"]

        for var in required_vars:
            if not os.getenv(var):
                raise EnvironmentError(f"❌ Missing required environment variable: {var}")

    except EnvironmentError as e:
        print(f"❌ Environment configuration error: {e}")
        exit(1)
