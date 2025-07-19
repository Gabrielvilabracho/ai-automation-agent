from services.openai_client import ask_gpt


def run_agent():
    print("🤖 Agente de automatización iniciado...")

    try:
        respuesta = ask_gpt("¿Qué puedo automatizar hoy?")

        if respuesta:
            print(f"💡 GPT sugiere: {respuesta}")
        else:
            print("❌ No se pudo obtener una respuesta de GPT")
            print("💡 Verifica tu configuración de API key en el archivo .env")

    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        print("💡 Revisa la configuración y conexión a internet")
