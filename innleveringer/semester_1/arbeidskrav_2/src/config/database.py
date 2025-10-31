from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

##
##  Used this to debug env variables
##
# Print what values are being loaded
## print("Environment variables:")
## print(f"DB_HOST: {os.getenv('DB_HOST')}")
## print(f"DB_USER: {os.getenv('DB_USER')}")
## print(f"DB_PASSWORD: {'*' * len(os.getenv('DB_PASSWORD', ''))}")
## print(f"DB_PORT: {os.getenv('DB_PORT')}")

# Database configuration dictionary
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": int(os.getenv("DB_PORT", 3306)),
    "database": os.getenv("DB_NAME", "")
}