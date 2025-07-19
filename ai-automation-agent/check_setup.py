#!/usr/bin/env python3
"""
Script de diagnóstico para verificar la configuración del proyecto
"""

import sys
from pathlib import Path


def check_python_version():
    """Verifica la versión de Python"""
    print("🐍 Verificando versión de Python...")
    version = sys.version_info
    print(f"   Python {version.major}.{version.minor}.{version.micro}")

    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("   ❌ Se requiere Python 3.8 o superior")
        return False
    else:
        print("   ✅ Versión de Python compatible")
        return True


def check_dependencies():
    """Verifica que las dependencias estén instaladas"""
    print("\n📦 Verificando dependencias...")

    required_packages = ["openai", "python-dotenv", "pytest"]

    missing_packages = []

    for package in required_packages:
        try:
            __import__(package.replace("-", "_"))
            print(f"   ✅ {package}")
        except ImportError:
            print(f"   ❌ {package} - NO INSTALADO")
            missing_packages.append(package)

    if missing_packages:
        print("\n   💡 Instala las dependencias faltantes:")
        print(f"   pip install {' '.join(missing_packages)}")
        return False

    return True


def check_env_file():
    """Verifica la configuración del archivo .env"""
    print("\n🔧 Verificando archivo .env...")

    env_file = Path(".env")

    if not env_file.exists():
        print("   ❌ Archivo .env no encontrado")
        print("   💡 Copia env.example a .env y configura tu API key")
        return False

    # Verificar que no esté vacío
    content = env_file.read_text().strip()
    if not content:
        print("   ❌ Archivo .env está vacío")
        return False

    # Verificar API key
    if "OPENAI_API_KEY=tu_api_key_aqui" in content:
        print("   ❌ API key no configurada (usando valor por defecto)")
        return False

    if "OPENAI_API_KEY=" in content:
        print("   ✅ API key configurada")
        return True
    else:
        print("   ❌ OPENAI_API_KEY no encontrada en .env")
        return False


def check_project_structure():
    """Verifica la estructura del proyecto"""
    print("\n📁 Verificando estructura del proyecto...")

    required_files = [
        "src/core/agent.py",
        "src/services/openai_client.py",
        "src/utils/config.py",
        "main.py",
        "requirements.txt",
    ]

    missing_files = []

    for file_path in required_files:
        if Path(file_path).exists():
            print(f"   ✅ {file_path}")
        else:
            print(f"   ❌ {file_path} - NO ENCONTRADO")
            missing_files.append(file_path)

    return len(missing_files) == 0


def main():
    """Función principal de diagnóstico"""
    print("🔍 DIAGNÓSTICO DEL PROYECTO AI AUTOMATION AGENT")
    print("=" * 50)

    checks = [
        check_python_version(),
        check_dependencies(),
        check_env_file(),
        check_project_structure(),
    ]

    print("\n" + "=" * 50)
    print("📊 RESUMEN DEL DIAGNÓSTICO")
    print("=" * 50)

    passed = sum(checks)
    total = len(checks)

    if passed == total:
        print("🎉 ¡Todo está configurado correctamente!")
        print("💡 Puedes ejecutar: python main.py")
    else:
        print(f"⚠️  {passed}/{total} verificaciones pasaron")
        print("🔧 Corrige los problemas antes de continuar")

    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
