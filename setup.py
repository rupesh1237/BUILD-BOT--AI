#!/usr/bin/env python3
"""
Setup script for AI Brick Cement Chatbot
"""
import os
import subprocess
import sys

def create_virtual_environment():
    """Create and activate virtual environment"""
    print("Creating virtual environment...")
    
    # Create virtual environment
    subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
    
    # Determine activation script path based on OS
    if os.name == 'nt':  # Windows
        activate_script = os.path.join("venv", "Scripts", "activate.bat")
        pip_path = os.path.join("venv", "Scripts", "pip")
    else:  # Unix/Linux/macOS
        activate_script = os.path.join("venv", "bin", "activate")
        pip_path = os.path.join("venv", "bin", "pip")
    
    print(f"Virtual environment created. Activate with: {activate_script}")
    
    # Install requirements
    print("Installing requirements...")
    subprocess.run([pip_path, "install", "-r", "requirements.txt"], check=True)
    
    print("Setup complete!")
    print("\nTo activate the virtual environment:")
    if os.name == 'nt':
        print("  venv\\Scripts\\activate")
    else:
        print("  source venv/bin/activate")
    
    print("\nTo run the application:")
    print("  python app.py")

if __name__ == "__main__":
    create_virtual_environment()