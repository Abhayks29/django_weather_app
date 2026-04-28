#!/usr/bin/env python
"""
Installation and setup script for Django Weather App
Run: python setup.py
"""

import os
import sys
import subprocess


def print_header(text):
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60 + "\n")


def run_command(command, description):
    """Run a shell command with error handling"""
    print(f"📌 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed!\n")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e.stderr}\n")
        return False


def main():
    print_header("🌤️ Django Weather App - Setup")
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ is required!")
        sys.exit(1)
    
    print("✅ Python version check passed\n")
    
    # Create virtual environment
    if not os.path.exists('venv'):
        print_header("Step 1: Creating Virtual Environment")
        if not run_command("python3 -m venv venv", "Creating virtual environment"):
            sys.exit(1)
    else:
        print("✅ Virtual environment already exists\n")
    
    # Activate venv (for subsequent commands)
    venv_python = os.path.join('venv', 'bin', 'python')
    venv_pip = os.path.join('venv', 'bin', 'pip')
    
    # Install requirements
    print_header("Step 2: Installing Dependencies")
    if not run_command(f"{venv_pip} install -r requirements.txt", "Installing packages"):
        sys.exit(1)
    
    # Run migrations
    print_header("Step 3: Setting Up Database")
    if not run_command(f"{venv_python} manage.py migrate", "Running migrations"):
        sys.exit(1)
    
    print_header("Step 4: Configuration Required")
    print("📝 IMPORTANT: Get your OpenWeatherMap API key")
    print("\n   1. Visit: https://openweathermap.org/api")
    print("   2. Sign up for a free account")
    print("   3. Get your API key from the dashboard")
    print("   4. Edit: weatherproject/settings.py")
    print("   5. Replace: WEATHER_API_KEY = 'your-openweathermap-api-key'")
    print("      with your actual API key\n")
    
    # Ask to create superuser
    print_header("Step 5: Create Admin User (Optional)")
    response = input("Do you want to create a superuser account? (y/n): ").lower()
    if response == 'y':
        os.system(f"source venv/bin/activate && {venv_python} manage.py createsuperuser")
    
    # Display completion message
    print_header("✅ Setup Complete!")
    print("""
Next steps:

1. ⚙️  Configure API Key:
   Edit weatherproject/settings.py and set your OpenWeatherMap API key

2. 🚀 Start the server:
   source venv/bin/activate
   python manage.py runserver

3. 🌐 Open in browser:
   http://127.0.0.1:8000

4. 👨‍💼 Admin panel:
   http://127.0.0.1:8000/admin/

📚 For more help, see:
   - README.md - Full documentation
   - QUICKSTART.md - Quick start guide
""")


if __name__ == "__main__":
    main()
