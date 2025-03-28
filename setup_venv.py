import venv
import os
import sys

# Create a virtual environment in the current directory
venv_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "venv")
print(f"Creating virtual environment in: {venv_dir}")

# Create the venv with pip installed
venv.create(venv_dir, with_pip=True)

print("Virtual environment created successfully!")
print("To activate, run: source activate.sh") 