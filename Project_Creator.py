import os
import platform


class ProjectCreator:
    """
    A class to manage the creation of a Python project structure.
    """

    def __init__(self, project_name):
        """
        Initializes the ProjectCreator with the project name.

        Args:
            project_name (str): The name of the project.
        """
        self.project_name = project_name
        self.project_dir = os.path.join(os.getcwd(), project_name)

    def create_directory(self, path, exist_ok=True):
        """
        Creates a directory.

        Args:
            path (str): The path of the directory to create.
            exist_ok (bool, optional): If True, do not raise an error if the directory exists. Defaults to True.
        """
        os.makedirs(path, exist_ok=exist_ok)
        print(f"Created directory: {path}")

    def create_file(self, path, content=""):
        """
        Creates a file with the given content.

        Args:
            path (str): The path of the file to create.
            content (str, optional): The content to write to the file. Defaults to "".
        """
        with open(path, "w") as f:
            f.write(content)
        print(f"Created: {path}")

    def create_project_directory(self):
        """Creates the main project directory."""
        self.create_directory(self.project_dir)

    def create_main_file(self):
        """Creates the main application file (main.py)."""
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
        self.create_file(os.path.join(
            self.project_dir, "main.py"), main_py_content)

    def create_test_file(self):
        """Creates the test application file (test_main.py)."""
        test_main_py_content = """
import os
from dotenv import load_dotenv

load_dotenv()
# openai_api_key = os.getenv("OPENAI_API_KEY")

def add(x, y):
    return x + y
def test_add_positive_numbers():
    assert add(2, 3) == 5
"""
        self.create_file(os.path.join(self.project_dir,
                         "test_main.py"), test_main_py_content)

    def create_env_file(self):
        """Creates the .env file."""
        self.create_file(os.path.join(self.project_dir, ".env"),
                         "# Environment variables go here\n")

    def create_requirements_file(self):
        """Creates the requirements.txt file."""
        requirements_content = "# List your project dependencies here\ndotenv\npitest\n"
        self.create_file(os.path.join(self.project_dir,
                         "requirements.txt"), requirements_content)

    def create_gitignore_file(self):
        """Creates the .gitignore file."""
        gitignore_content = """
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
#  For a library or package, you might want to ignore these files since the code is
#  intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#  According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#  However, in case of collaboration, if having platform-specific dependencies or dependencies
#  having no cross-platform support, pipenv may install dependencies that don't work, or not
#  install all needed dependencies.
#Pipfile.lock

# UV
#  Similar to Pipfile.lock, it is generally recommended to include uv.lock in version control.
#  This is especially recommended for binary packages to ensure reproducibility, and is more
#  commonly ignored for libraries.
#uv.lock

# poetry
#  Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#  This is especially recommended for binary packages to ensure reproducibility, and is more
#  commonly ignored for libraries.
#  https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#  Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#  pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#  in version control.
#  https://pdm.fming.dev/latest/usage/project/#working-with-version-control
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
        self.create_file(os.path.join(self.project_dir,
                         ".gitignore"), gitignore_content)

    def create_readme_file(self):
        """Creates the README.md file."""
        readme_content = f"""# {self.project_name.capitalize()}

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
        self.create_file(os.path.join(
            self.project_dir, "README.md"), readme_content)

    def create_src_directory(self):
        """Creates the src directory."""
        src_dir = os.path.join(self.project_dir, "src")
        self.create_directory(src_dir)
        self.create_file(os.path.join(src_dir, "__init__.py")
                         )  # Create an empty __init__.py

    def create_batch_files(self):
        """Creates the batch files for Windows."""
        if platform.system() == "Windows":
            # 000_init.bat
            self.create_file(os.path.join(self.project_dir, "000_init.bat"),
                             "@echo off\n"
                             "REM Change your name\n"
                             "git config --global user.name 'SHAN Konduru'\n"
                             "REM Change your email id\n"
                             "git config --global user.email 'ShanKonduru@gmail.com'\n"
                             "git init\n")

            # 001_env.bat
            self.create_file(os.path.join(self.project_dir, "001_env.bat"),
                             "@echo off\n"
                             "python -m venv .venv\n")

            # 002_activate.bat
            self.create_file(os.path.join(self.project_dir, "002_activate.bat"),
                             "@echo off\n"
                             ".\\.venv\\Scripts\\activate\n")

            # 003_setup.bat
            self.create_file(os.path.join(self.project_dir, "003_setup.bat"),
                             "@echo off\n"
                             "python.exe -m pip install --upgrade pip\n"
                             "pip install -r requirements.txt\n")

            # 004_run.bat
            self.create_file(os.path.join(self.project_dir, "004_run.bat"),
                             "@echo off\n"
                             "python main.py\n")
            # 005_run_test.bat
            self.create_file(os.path.join(self.project_dir, "005_run_test.bat"),
                             "@echo off\n"
                             "pytest\n")
            # 008_deactivate.bat
            self.create_file(os.path.join(self.project_dir, "008_deactivate.bat"),
                             "@echo off\n"
                             ".\\.venv\\Scripts\\deactivate\n")
        else:
            print("\nBatch file creation skipped (only supported on Windows).")

    def create_project_files(self):
        """
        Creates all the project files and directories.
        """
        self.create_project_directory()
        self.create_main_file()
        self.create_test_file()
        self.create_env_file()
        self.create_requirements_file()
        self.create_gitignore_file()
        self.create_readme_file()
        self.create_src_directory()
        self.create_batch_files()
        print("\nProject structure generated successfully!")


if __name__ == "__main__":
    project_name = input("Enter the name of your project: ")
    creator = ProjectCreator(project_name)
    creator.create_project_files()
