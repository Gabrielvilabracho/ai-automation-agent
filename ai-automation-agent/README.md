# AI Automation Agent

An intelligent automation agent built with Python, OpenAI, and n8n to create automated workflows.

## Project Status

### Completed
- [x] **Professional project structure** with organized folders (`src/`, `tests/`, etc.)
- [x] **Virtual environment configured** with development and production dependencies
- [x] **Tests working** (3 tests passing successfully)
- [x] **VS Code/Cursor configuration** ready for development and debugging
- [x] **Local Git repository** initialized with commits
- [x] **GitHub repository** created and connected
- [x] **GitLens configured** for history visualization
- [x] **Development tools configured** (Black, isort, pylint, pytest)

### In Progress
- [ ] **Complete GitHub synchronization** (resolve submodule issue)
- [ ] **Project documentation** (this README)

### Next Steps
- [ ] **Define first automation objective**
- [ ] **Create agent endpoint/script**
- [ ] **Install and configure n8n**
- [ ] **Create first automation workflow**
- [ ] **Integrate with MCP (if applicable)**

---

## Project Roadmap

### **Phase 1: Base Configuration** ✅
- [x] Configure Python project structure
- [x] Configure virtual environment and dependencies
- [x] Configure VS Code/Cursor for development
- [x] Configure Git and GitHub
- [x] Configure code quality tools
- [x] Create basic tests

### **Phase 2: Agent Development** 🔄
- [ ] Define specific use cases
- [ ] Create API endpoints for the agent
- [ ] Implement OpenAI integration
- [ ] Create configuration system
- [ ] Implement logging and monitoring

### **Phase 3: n8n Integration** 📋
- [ ] Install and configure n8n
- [ ] Create basic workflows
- [ ] Connect agent with n8n
- [ ] Implement automatic triggers
- [ ] Create monitoring dashboards

### **Phase 4: Specific Automations** 📋
- [ ] Email automation
- [ ] Data processing
- [ ] External API integration
- [ ] Automatic notifications
- [ ] Automatic reports

### **Phase 5: Scalability and Production** 📋
- [ ] Project dockerization
- [ ] CI/CD configuration
- [ ] Monitoring and alerts
- [ ] Complete documentation
- [ ] Deployment guides

---

## Quick Setup

### Prerequisites
- Python 3.8 or higher
- pip
- Git
- VS Code/Cursor (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Gabrielvilabracho/ai-automation-agent.git
   cd ai-automation-agent
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

4. **Configure environment variables**
   ```bash
   cp env.example .env
   # Edit .env with your OpenAI credentials
   ```

5. **Run tests**
   ```bash
   PYTHONPATH=src pytest tests/ -v
   ```

---

## Project Structure

```
ai-automation-agent/
├── src/                    # Source code
│   ├── core/              # Main agent logic
│   │   └── agent.py       # Main agent function
│   ├── services/          # External services
│   │   └── openai_client.py # OpenAI client
│   └── utils/             # Utilities
│       ├── config.py      # Configuration
│       └── helpers.py     # Helper functions
├── tests/                 # Unit tests
│   └── test_basic.py      # Basic tests
├── .vscode/               # VS Code configuration
├── main.py               # Entry point
├── requirements.txt      # Production dependencies
├── requirements-dev.txt  # Development dependencies
├── pyproject.toml       # Tool configuration
├── .pre-commit-config.yaml # Pre-commit hooks
└── README.md            # This file
```

---

## Testing

```bash
# Run all tests
PYTHONPATH=src pytest tests/ -v

# Run tests with coverage
PYTHONPATH=src pytest --cov=src tests/

# Run specific tests
PYTHONPATH=src pytest tests/test_basic.py -v
```

---

## Development

### Useful Commands

- **Run application**: `python main.py`
- **Format code**: `black src/ tests/ main.py`
- **Sort imports**: `isort src/ tests/ main.py`
- **Lint code**: `pylint src/ tests/ main.py`

### VS Code/Cursor Tasks

Use `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) and search for:
- `Tasks: Run Task` → Select the desired task
- `Debug: Start Debugging` → Select debug configuration

---

## Cursor Configuration

This project is configured to work perfectly with Cursor:

- **Python interpreter**: Configured to use virtual environment
- **Automatic formatting**: Black runs on save
- **Linting**: Pylint and Flake8 configured
- **Debugging**: Ready-to-use debug configurations
- **Testing**: pytest integration

### Recommended Extensions

Extensions will be automatically installed when you open the project in Cursor.

---

## Project Metrics

- **Lines of code**: ~200+
- **Tests**: 3 basic tests passing
- **Dependencies**: 20+ packages configured
- **Development tools**: 8+ tools configured

---

## Contributing

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

This project is under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Support

If you have problems or questions:
1. Check the documentation
2. Search existing issues
3. Create a new issue with problem details

---

## Development Notes

### Last Update
- **Date**: January 2025
- **Version**: 0.1.0
- **Status**: Base configuration completed, ready for agent development

### Next Sessions
- [ ] Resolve submodule issue in GitHub
- [ ] Define specific agent use cases
- [ ] Implement API endpoints
- [ ] Configure n8n for workflows
