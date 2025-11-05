from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database configuration dictionary
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "database": os.getenv("DB_NAME", "")
}