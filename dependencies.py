
import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_dependencies():
    required_packages = ['speech_recognition', 'google-cloud-texttospeech', 'pydub']
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"{package} is not installed. Installing...")
            install_package(package)
