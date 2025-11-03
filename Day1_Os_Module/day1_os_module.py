# -----------------------------
# DAY 1: Meet the OS Module
# Author: Temitayo Adedoyin
# -----------------------------

# The os module helps Python interact with your computer's operating system
import os

print("👋 Hello Temitayo! Welcome to your first automation project.\n")

# 1️⃣ Get the current working directory (the folder your script is running in)
current_dir = os.getcwd()
print(f"📂 Current working directory: {current_dir}\n")

# 2️⃣ List everything inside that folder
print("📄 Items in this folder right now:")
for item in os.listdir(current_dir):
    print("   •", item)
print()

# 3️⃣ Create three new folders automatically
folders = ["Images", "Documents", "Videos"]

for folder in folders:
    path = os.path.join(current_dir, folder)   # create full path
    if not os.path.exists(path):               # only make it if it doesn't exist
        os.mkdir(path)
        print(f"✅ Created folder: {folder}")
    else:
        print(f"⚠️ Folder already exists: {folder}")

print()

# 4️⃣ Create an empty file inside each folder
for folder in folders:
    file_path = os.path.join(current_dir, folder, f"{folder}_sample.txt")
    with open(file_path, "w") as f:            # open in write mode
        f.write(f"This is a sample file in the {folder} folder.")
    print(f"📝 Created file inside {folder}: {folder}_sample.txt")

print("\n🎉 All done! You just automated folder and file creation on your computer.")
