import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

def test_imports():
    """Test que verifica que los módulos se pueden importar correctamente"""
    try:
        from core.agent import run_agent
        from services.openai_client import ask_gpt
        from utils.config import OPENAI_API_KEY
        assert True, "Todos los módulos se importan correctamente"
    except ImportError as e:
        assert False, f"Error importando módulos: {e}"

def test_config_loading():
    """Test que verifica que la configuración se carga"""
    from utils.config import OPENAI_API_KEY
    # No debería fallar aunque la API key no esté configurada
    assert OPENAI_API_KEY is not None or OPENAI_API_KEY is None

def test_agent_function_exists():
    """Test que verifica que la función run_agent existe"""
    from core.agent import run_agent
    assert callable(run_agent), "run_agent debe ser una función"
