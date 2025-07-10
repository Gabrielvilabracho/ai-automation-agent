from services.openai_client import ask_gpt

def run_agent():
    print("Agente iniciado.")
    respuesta = ask_gpt("¿Qué puedo automatizar hoy?")
    print(f"GPT responde: {respuesta}")
