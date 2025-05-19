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
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
"""
    with open(os.path.join(project_name, "main.py"), "w") as f:
        f.write(main_py_content)
    print(f"Created: {os.path.join(project_name, 'main.py')}")

    # Create the .env file
    with open(os.path.join(project_name, ".env"), "w") as f:
        f.write("# Environment variables go here\n")
    print(f"Created: {os.path.join(project_name, '.env')}")

    # Create the requirements.txt file
    with open(os.path.join(project_name, "requirements.txt"), "w") as f:
        f.write("# List your project dependencies here\n")
    print(f"Created: {os.path.join(project_name, 'requirements.txt')}")

    # Create the .gitignore file
    with open(os.path.join(project_name, ".gitignore"), "w") as f:
        f.write("# Ignore Python cache files\n__pycache__/\n*.pyc\n*.pyo\n\n# Ignore environment files\n.env\n\n# Ignore IDE specific files\n.idea/\n.vscode/\n")
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
* `005_deactivate.bat`: Deactivates the currently active virtual environment.

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
            f.write(f"git config --global user.name 'SHAN Konduru'\n")
            f.write(f"git config --global user.email 'ShanKonduru@gmail.com'\n")
            f.write(f"git init'\n")
        print(f"Created: {os.path.join(project_name, '000_init.bat')}")

        # 001_env.bat
        with open(os.path.join(project_name, "001_env.bat"), "w") as f:
            f.write(f"@echo off\n")
            f.write(f"python -m venv venv\n")
        print(f"Created: {os.path.join(project_name, '001_env.bat')}")

        # 002_activate.bat
        with open(os.path.join(project_name, "002_activate.bat"), "w") as f:
            f.write(f"@echo off\n")
            f.write(f".\\venv\\Scripts\\activate\n")
        print(f"Created: {os.path.join(project_name, '002_activate.bat')}")

        # 003_setup.bat
        with open(os.path.join(project_name, "003_setup.bat"), "w") as f:
            f.write(f"@echo off\n")
            f.write(f"pip install -r requirements.txt\n")
        print(f"Created: {os.path.join(project_name, '003_setup.bat')}")

        # 004_run.bat
        with open(os.path.join(project_name, "004_run.bat"), "w") as f:
            f.write(f"@echo off\n")
            f.write(f"python main.py\n")
        print(f"Created: {os.path.join(project_name, '004_run.bat')}")

        # 005_deactivate.bat
        with open(os.path.join(project_name, "005_deactivate.bat"), "w") as f:
            f.write(f"@echo off\n")
            f.write(f".\\venv\\Scripts\\deactivate\n")
        print(f"Created: {os.path.join(project_name, '005_deactivate.bat')}")
    else:
        print("\nBatch file creation skipped (only supported on Windows).")

    print("\nProject structure generated successfully!")

if __name__ == "__main__":
    project_name = input("Enter the name of your project: ")
    create_project_files(project_name)