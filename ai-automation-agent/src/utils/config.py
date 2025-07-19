import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def validate_api_key():
    """Valida que la API key esté configurada"""
    if not OPENAI_API_KEY:
        raise ValueError(
            "OPENAI_API_KEY no está configurada. "
            "Por favor, crea un archivo .env con tu API key de OpenAI."
        )
    return OPENAI_API_KEY
