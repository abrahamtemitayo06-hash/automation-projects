# Smart Folder Creator with Logging (Pro Version)

import os 
from datetime import datetime 

print("Starting Smart Folder creator(Pro Version)...\n")

# Step 1: Always work from the script's own folder---  
base_dir = os.path.dirname(os.path.abspath(__file__))
print(f" Working in:{base_dir}\n")

# Step 2: Folder list(can include subfolders)---
folders = ["photos","Videos","Projects/ClientA","Projects/ClientB","Research","Backups"]

# Step 3: Prepare logging file---
log_file = os.path.join(base_dir,"Folder_creator.log")
created_count = 0
skipped_count = 0

def log_message(message):
    """ Write messages to both console and log file."""
    print(message)
    with open(log_file,"a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%M-%D %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")
for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    if os.path.exists(folder_path):
        log_message(f"{folder} already exists. Skipping...")
        skipped_count += 1
    else:
        try:
            os.makedirs(folder_path, exist_ok=True)
            log_message(f"{folder} successfully created!")
            created_count += 1
        except Exception as e:
            log_message(f"Could not create {folder}- Error: {e}")

print("\n Summary")
print(f"Created: {created_count}")
print(f"Skipped: {skipped_count}")
print("\n All tasks completed successfully!")

log_message("------SESSION ENDED-----")