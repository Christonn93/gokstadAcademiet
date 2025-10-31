from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(dotenv_path='../../.env')

# Database configuration dictionary
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD")
}