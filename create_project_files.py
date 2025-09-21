import os
import platform

def create_project_files(project_name):
    """
    Creates common project files and directories for a Python project,
    including basic batch files for Windows.

    Args:
        project_name (str): The name of the project directory to create.
    """

    # Create the main project directory
    os.makedirs(project_name, exist_ok=True)
    print(f"Created project directory: {project_name}")

    # Create the main application file
    main_py_content = """
import os
from dotenv import load_dotenv

load_dotenv()
# openai_api_key = os.getenv("OPENAI_API_KEY")

def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
"""
    with open(os.path.join(project_name, "main.py"), "w") as f:
        f.write(main_py_content)
    print(f"Created: {os.path.join(project_name, 'main.py')}")


    # Create the main application file
    test_main_py_content = """
import os
from dotenv import load_dotenv
import pytest

load_dotenv()
# openai_api_key = os.getenv("OPENAI_API_KEY")

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def subtract(x, y):
    return x - y

@pytest.mark.positive
def test_add_positive():
    assert add(2, 3) == 5

@pytest.mark.positive
def test_subtract_positive():
    assert subtract(10, 4) == 6

@pytest.mark.positive
def test_multiply_positive():
    assert multiply(5, 6) == 30

@pytest.mark.positive
def test_divide_positive():
    assert divide(10, 2) == 5

@pytest.mark.edge
def test_add_with_zero():
    assert add(5, 0) == 5

@pytest.mark.edge
def test_subtract_with_zero():
    assert subtract(10, 0) == 10

@pytest.mark.edge
def test_add_with_negative_numbers():
    assert add(-2, -3) == -5

@pytest.mark.edge
def test_multiply_by_zero():
    assert multiply(100, 0) == 0

@pytest.mark.edge
def test_divide_negative_numbers():
    assert divide(-10, -2) == 5
"""
    # Create a 'src' directory (optional, but good practice)
    tests_dir = os.path.join(project_name, "tests")
    os.makedirs(tests_dir, exist_ok=True)
    with open(os.path.join(tests_dir, "__init__.py"), "w") as f:
        pass  # Create an empty __init__.py to make it a package
    print(f"Created directory: {tests_dir}")
    print(f"Created: {os.path.join(tests_dir, '__init__.py')}")

    with open(os.path.join(project_name, "tests\\test_main.py"), "w") as f:
        f.write(test_main_py_content)
    print(f"Created: {os.path.join(project_name, 'tests\\test_main.py')}")

    # create pytest.ini file
    pytest_ini_content = """
[pytest]
markers=
    unit: Unit tests for individual functions
    integration: Integration tests between components
    smoke: Quick smoke tests
    regression: Regression tests to prevent feature breakage
    performance: Performance and load tests
    security: Security-related tests
    edge: Edge case tests
    negative: Negative tests to ensure proper error handling
    positive: Positive tests to ensure expected behavior
    api: API endpoint tests        
    db: Database-related tests
    ui: User interface tests
    e2e: End-to-end tests
    functional: Functional tests for specific features
    """
    with open(os.path.join(project_name, "tests\\pytest.ini"), "w") as f:
        f.write(pytest_ini_content)
    print(f"Created: {os.path.join(project_name, 'tests\\pytest.ini')}")

    with open(os.path.join(project_name, "pytest.ini"), "w") as f:
        f.write(pytest_ini_content)
    print(f"Created: {os.path.join(project_name, 'pytest.ini')}")

    # Create the .env file
    with open(os.path.join(project_name, ".env"), "w") as f:
        f.write("# Environment variables go here\n")
    print(f"Created: {os.path.join(project_name, '.env')}")

    # Create the requirements.txt file
    with open(os.path.join(project_name, "requirements.txt"), "w") as f:
        f.write("# List your project dependencies here\n")
        f.write("dotenv\n")
        f.write("pytest\n")
        f.write("pytest-html\n")
    print(f"Created: {os.path.join(project_name, 'requirements.txt')}")

    # Create the .gitignore file
    ignore_content = """
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# UV
#   Similar to Pipfile.lock, it is generally recommended to include uv.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#uv.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/latest/usage/project/#working-with-version-control
.pdm.toml
.pdm-python
.pdm-build/

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/

# Ruff stuff:
.ruff_cache/

# PyPI configuration file
.pypirc
    """
    with open(os.path.join(project_name, ".gitignore"), "w") as f:
        f.write(ignore_content)
    print(f"Created: {os.path.join(project_name, '.gitignore')}")

    # Create an enhanced README.md file
    readme_content = f"""# {project_name.capitalize()}

## Description

[Briefly describe your project here.]

## Installation


1.  **Initialize git (Windows):**
    Run the `000_init.bat` file.

2.  **Create a virtual environment (Windows):**
    Run the `001_env.bat` file.

3.  **Activate the virtual environment (Windows):**
    Run the `002_activate.bat` file.

4.  **Install dependencies:**
    Run the `003_setup.bat` file. This will install all the packages listed in `requirements.txt`.

5.  **Deactivate the virtual environment (Windows):**
    Run the `005_deactivate.bat` file.

## Usage

1.  **Run the main application (Windows):**
    Run the `004_run.bat` file.

    [Provide instructions on how to use your application.]

## Batch Files (Windows)

This project includes the following batch files to help with common development tasks on Windows:

* `000_init.bat`: Initialized git and also usn and pwd config setup also done.
* `001_env.bat`: Creates a virtual environment named `venv`.
* `002_activate.bat`: Activates the `venv` virtual environment.
* `003_setup.bat`: Installs the Python packages listed in `requirements.txt` using `pip`.
* `004_run.bat`: Executes the main Python script (`main.py`).
* `005_run_test.bat`: Executes the pytest  scripts (`test_main.py`).
* `008_deactivate.bat`: Deactivates the currently active virtual environment.

## Contributing

[Explain how others can contribute to your project.]

## License

[Specify the project license, if any.]
"""
    with open(os.path.join(project_name, "README.md"), "w") as f:
        f.write(readme_content)
    print(f"Created: {os.path.join(project_name, 'README.md')}")

    # Create a 'src' directory (optional, but good practice)
    src_dir = os.path.join(project_name, "src")
    os.makedirs(src_dir, exist_ok=True)
    with open(os.path.join(src_dir, "__init__.py"), "w") as f:
        pass  # Create an empty __init__.py to make it a package
    print(f"Created directory: {src_dir}")
    print(f"Created: {os.path.join(src_dir, '__init__.py')}")

    # Create the batch files for Windows
    if platform.system() == "Windows":
        # 000_init.bat
        with open(os.path.join(project_name, "000_init.bat"), "w") as f:
            f.write(f"@echo off\n")
            f.write(f"REM Chainge your name\n")
            f.write(f"git config --global --replace-all user.name 'SHAN Konduru'\n")
            f.write(f"REM Chainge your email id \n")
            f.write(f"git config --global --replace-all user.email 'ShanKonduru@gmail.com' \n")
            f.write(f"git init\n")
        print(f"Created: {os.path.join(project_name, '000_init.bat')}")

        # 001_env.bat
        with open(os.path.join(project_name, "001_env.bat"), "w") as f:
            f.write(f"@echo off\n")
            f.write(f"python -m venv .venv\n")
        print(f"Created: {os.path.join(project_name, '001_env.bat')}")

        # 002_activate.bat
        with open(os.path.join(project_name, "002_activate.bat"), "w") as f:
            f.write(f"@echo off\n")
            f.write(f".\\.venv\\Scripts\\activate\n")
        print(f"Created: {os.path.join(project_name, '002_activate.bat')}")

        # 003_setup.bat
        with open(os.path.join(project_name, "003_setup.bat"), "w") as f:
            f.write(f"@echo off\n")
            f.write(f"python -m pip install --upgrade pip\n")
            f.write(f"pip install -r requirements.txt\n")
        print(f"Created: {os.path.join(project_name, '003_setup.bat')}")

        # 004_run.bat
        with open(os.path.join(project_name, "004_run.bat"), "w") as f:
            f.write(f"@echo off\n")
            f.write(f"python main.py\n")
        print(f"Created: {os.path.join(project_name, '004_run.bat')}")

        # 005_run_test.bat
        with open(os.path.join(project_name, "005_run_test.bat"), "w") as f:
            f.write(f"@echo off\n")
            f.write(f"pytest --html=test_reports\\report.html --self-contained-html tests\\\n")
        print(f"Created: {os.path.join(project_name, '005_run_test.bat')}")

        # 008_deactivate.bat
        with open(os.path.join(project_name, "008_deactivate.bat"), "w") as f:
            f.write(f"@echo off\n")
            f.write(f".\\.venv\\Scripts\\deactivate\n")
        print(f"Created: {os.path.join(project_name, '008_deactivate.bat')}")
    else:
        print("\nBatch file creation skipped (only supported on Windows).")

    print("\nProject structure generated successfully!")

if __name__ == "__main__":
    project_name = input("Enter the name of your project: ")
    create_project_files(project_name)
