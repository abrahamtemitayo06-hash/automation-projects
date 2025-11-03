import os 
from datetime import datetime 

# Base directory for this project

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOG_DIR = os.path.join(BASE_DIR,"logs")

ACTIVITY_DIR = os.path.join(LOG_DIR,"activities")

ERROR_DIR = os.path.join(LOG_DIR,"errors")

# Ensure folders exist 

os.makedirs(ACTIVITY_DIR, exist_ok=True)
os.makedirs(ERROR_DIR, exist_ok=True)

def write_log(message):
    log_file = os.path.join(ACTIVITY_DIR,f"activity_{datetime.now().date()}.txt")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file,"a",encoding="utf-8") as file:
        file.write(f"[{timestamp}] {message}\n")

def log_error(message):
    error_log_file = os.path.join(ERROR_DIR,f"errors_{datetime.now().date()}.txt")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(error_log_file,"a",encoding="utf-8") as file:
        file.write(f"[{timestamp}] ERROR: {message}\n")