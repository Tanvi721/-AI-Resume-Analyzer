import subprocess
import sys
import time

def run():
    print("🚀 Starting AI Resume Analyzer Suite...")
    
    # 1. Start FastAPI Backend
    print("📡 Launching FastAPI Backend on Port 8000...")
    backend = subprocess.Popen([sys.executable, "-m", "uvicorn", "main:app", "--reload", "--port", "8000"])
    
    # Give the backend a moment to initialize
    time.sleep(3)
    
    # 2. Start Streamlit Frontend
    print("💻 Launching Streamlit Frontend...")
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
    except KeyboardInterrupt:
        print("\nStopping servers...")
        backend.terminate()

if __name__ == "__main__":
    run()