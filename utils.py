import os
from dotenv import load_dotenv


def load_api_key():
    """
    Load the API key from the .env file.

    :return: API key as a string
    """
    load_dotenv()
    api_key = os.getenv('SECRET_KEY')
    if not api_key:
        raise ValueError("API key not found. Make sure it's set in the .env file.")
    return api_key