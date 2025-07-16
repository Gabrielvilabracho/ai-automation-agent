from src.services.openai_client import ask_gpt


def test_ask_gpt():
    response = ask_gpt("¿Qué puedo automatizar hoy?")
    assert response is not None
    assert "automatizar" in response.lower()
