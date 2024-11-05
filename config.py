import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Paths
DOCUMENTS_FOLDER = os.getenv("DOCUMENTS_FOLDER", "data/documents/")
LOGS_FOLDER = os.getenv("LOGS_FOLDER", "logs/")
API_KEY = os.getenv("API_KEY", "your_api_key_here")

# Logging configuration
LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")
