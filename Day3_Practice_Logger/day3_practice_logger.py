from datetime import datetime 

def my_logger(text):
    """Logs text messages with timestamp into a file"""
    try:
        with open("activity_log.txt", "a",encoding = "utf-8") as f:
            timestamp = datetime.now().strftime("%Y-%M-%D %H:%M:%S")
            f.write(f"[{timestamp}] {text}\n")
            print(f"Logged: {text}")
    except Exception as e:
        print(f"Error writing to file: {e}")

my_logger("Started Practicing Logging")
my_logger("Created my first custom function!")
my_logger("Feeling more confident about automation")
my_logger("Day 3 practice completed successfully!")
my_logger("I've got this!")
