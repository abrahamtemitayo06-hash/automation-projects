import os 
from datetime import datetime 

def log_message (message):
    """Logs messages into daily log files inside a 'logs' folder."""
    # Step 1: ensure a logs folder exists
    daily_logs = "logs"
    if not os.path.exists(daily_logs):
        os.mkdir(daily_logs)
        print("'logs' folder created.")
    
    # Step 2: Create a log file based on today's date 
    date_today = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join(daily_logs, f"{date_today}.txt")

    # Step 3: Write message into the log file
    try:
        with open(log_file, "a",encoding = "utf-8") as file:
            timestamp = datetime.now().strftime("%Y-%M-%D %H:%M:%S")
            file.write(f"[{timestamp}] {message}\n")
            print(f"Logged: {message}")
    except Exception as e:
        print(f" Error writing to file: {e}")

log_message("Started Day 3 Level 2 pactice.")
log_message("Automatically created a folder for logs.")
log_message("Saved messages with timestamps into today's file.")
log_message("This is an extra log entry I added myself.")
log_message("let's see what happens")
        