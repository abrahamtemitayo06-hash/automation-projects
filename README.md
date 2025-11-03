# automation-projects
a collection of my python automation projects - file sorting, Excel cleaning, email automation and more.
# 🗂️ Day 1: File Organizer – Python Automation

### 📌 Overview
This is a simple Python automation script that organizes files in a folder into subfolders based on their file types (e.g., Documents, Images, Audio, etc.).  
It was my first project in learning **Python for automation**.

---

### ⚙️ Features
- Automatically detects file types using Python’s `os` and `shutil` modules.  
- Moves files into categorized folders.  
- Prevents overwriting existing files.  
- Provides a summary of how many files were sorted.

---

### 🧠 What I Learned
- How to use the **OS module** to navigate folders and handle file paths.  
- How to use **conditional logic** to classify files by extension.  
- How to make automation scripts more dynamic and reusable.

---

### 🧰 Tools & Technologies
- **Python 3**
- **VS Code**
- Modules: `os`, `shutil`

---

### 🚀 How to Run
1. Clone or download this repository.
2. Open the folder in VS Code or your preferred editor.
3. Place some files inside the folder you want to organize.
4. Run the script:
   ```bash

## EXAMPLE OUTPUT
Documents moved: 3
Images moved: 5
Audio moved: 2
Unknown files: 1

   
   python day1_os_module.py
