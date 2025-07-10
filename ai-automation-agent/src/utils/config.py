import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Este print puedes borrarlo después
print(f"API Key cargada: {OPENAI_API_KEY}")
