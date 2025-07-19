from openai import OpenAI
from utils.config import validate_api_key


def ask_gpt(prompt):
    try:
        api_key = validate_api_key()
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content
    except ValueError as e:
        print(f"Error de configuración: {e}")
        return None
    except Exception as e:
        print(f"Error al comunicarse con OpenAI: {e}")
        return None
