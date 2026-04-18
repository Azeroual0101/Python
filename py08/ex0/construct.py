import os
import site
import sys


def show_global_status() -> None:
    print("MATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env\\Scripts\\activate     # On Windows")
    print("\nThen run this program again.")


def show_venv_status() -> None:
    venv_path = sys.prefix
    venv_name = os.path.basename(venv_path)

    print("MATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")

    packages_path = site.getsitepackages()[0]
    print("Package installation path:")
    print(packages_path)


def main() -> None:
    if sys.prefix != sys.base_prefix:
        show_venv_status()
    else:
        show_global_status()


if __name__ == "__main__":
    main()
