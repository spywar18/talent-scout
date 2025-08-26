# hiring-assistant/utils.py

import os
from dotenv import load_dotenv

def load_api_key():
    """
    Loads the Google API key from a .env file.
    
    Raises:
        ValueError: If the GOOGLE_API_KEY is not found in the environment variables.
    """
    # Load environment variables from a .env file if it exists
    load_dotenv()
    
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY not found. Please create a .env file in the root directory "
            "and add the following line:\n\n"
            "GOOGLE_API_KEY=\"your-google-api-key\""
        )
    return api_key
