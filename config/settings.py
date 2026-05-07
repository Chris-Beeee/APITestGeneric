import os
from dotenv import load_dotenv

# Load variables from .env file into the environment
load_dotenv()

class Settings:
    # Use os.getenv to pull from environment, with a fallback if needed
    BASE_URL = os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")
    API_KEY = os.getenv("API_KEY")
    TIMEOUT = int(os.getenv("TIMEOUT", 10))

settings = Settings()
