# Automating Repetitive Tasks
# Author: Temitayo Adedoyin

import os 
print("Starting Smart Folder Creator...\n")

base_dir = os.path.dirname(os.path.abspath(__file__))

folders = ["Photos","Videos","Projects","Research","Backups","Invoices","Notes"]

for folder in folders:
    folder_path = os.path.join(base_dir,folder)
    if os.path.exists(folder_path):
        print(f"'{folder}' already exists. Skipping...")
    else:
        try:
            os.mkdir(folder_path)
            print(f"Folder for {folder} created!")
        except Exception as e:
            print(f"Could not create {folder}-Error:{e}")
print("\n All tasks completed successfully!")