from openai import OpenAI
from utils.config import OPENAI_API_KEY


def ask_gpt(prompt):
    client = OpenAI(api_key=OPENAI_API_KEY)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
