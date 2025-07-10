# AI Automation Agent

Un agente de automatización inteligente construido con Python y OpenAI.

## 🚀 Configuración Rápida

### Prerrequisitos
- Python 3.8 o superior
- pip
- Git

### Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <tu-repositorio>
   cd ai-automation-agent
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

4. **Configurar variables de entorno**
   ```bash
   cp .env.example .env
   # Editar .env con tus credenciales
   ```

5. **Instalar pre-commit hooks**
   ```bash
   pre-commit install
   ```

## 🛠️ Desarrollo

### Comandos útiles

- **Ejecutar la aplicación**: `python main.py`
- **Ejecutar tests**: `pytest tests/ -v`
- **Formatear código**: `black src/ tests/ main.py`
- **Ordenar imports**: `isort src/ tests/ main.py`
- **Linting**: `pylint src/ tests/ main.py`

### Tareas de VS Code/Cursor

Usa `Ctrl+Shift+P` (o `Cmd+Shift+P` en Mac) y busca:
- `Tasks: Run Task` → Selecciona la tarea deseada
- `Debug: Start Debugging` → Selecciona la configuración de debug

## 📁 Estructura del Proyecto

```
ai-automation-agent/
├── src/                    # Código fuente
│   └── core/              # Lógica principal
├── tests/                 # Tests unitarios
├── main.py               # Punto de entrada
├── requirements.txt      # Dependencias de producción
├── requirements-dev.txt  # Dependencias de desarrollo
├── pyproject.toml       # Configuración de herramientas
└── .pre-commit-config.yaml # Hooks de pre-commit
```

## 🔧 Configuración de Cursor

Este proyecto está configurado para trabajar perfectamente con Cursor:

- **Interprete de Python**: Configurado para usar el entorno virtual
- **Formateo automático**: Black se ejecuta al guardar
- **Linting**: Pylint y Flake8 configurados
- **Debugging**: Configuraciones listas para debug
- **Tests**: Integración con pytest

### Extensiones recomendadas

Las extensiones se instalarán automáticamente cuando abras el proyecto en Cursor.

## 🧪 Testing

```bash
# Ejecutar todos los tests
pytest

# Ejecutar tests con coverage
pytest --cov=src

# Ejecutar tests específicos
pytest tests/test_specific.py
```

## 📦 Empaquetado

```bash
# Construir el paquete
python -m build

# Instalar en modo desarrollo
pip install -e .
```

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 🆘 Soporte

Si tienes problemas o preguntas:
1. Revisa la documentación
2. Busca en los issues existentes
3. Crea un nuevo issue con detalles del problema
