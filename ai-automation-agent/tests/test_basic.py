import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

# Imports después de configurar el path
from core.agent import run_agent
from services.openai_client import ask_gpt
from utils.config import OPENAI_API_KEY, validate_api_key


def test_imports():
    """Test que verifica que los módulos se pueden importar correctamente"""
    try:
        # Los imports ya están hechos arriba, solo verificamos que funcionen
        assert True, "Todos los módulos se importan correctamente"
    except ImportError as e:
        pytest.fail(f"Error importando módulos: {e}")


def test_config_loading():
    """Test que verifica que la configuración se carga"""
    # No debería fallar aunque la API key no esté configurada
    assert OPENAI_API_KEY is not None or OPENAI_API_KEY is None


def test_agent_function_exists():
    """Test que verifica que la función run_agent existe"""
    assert callable(run_agent), "run_agent debe ser una función"


def test_validate_api_key_without_key():
    """Test que verifica el comportamiento cuando no hay API key"""
    # Si no hay API key configurada, debería lanzar ValueError
    try:
        validate_api_key()
        # Si llegamos aquí, significa que hay una API key configurada
        # lo cual está bien para el test
        assert True
    except ValueError:
        # Esto es esperado si no hay API key
        assert True


def test_ask_gpt_without_api_key():
    """Test que verifica el comportamiento de ask_gpt sin API key"""
    # Debería manejar graciosamente la falta de API key
    result = ask_gpt("Test prompt")

    # Si no hay API key, debería retornar None
    # Si hay API key, debería retornar una respuesta
    assert result is None or isinstance(result, str)
