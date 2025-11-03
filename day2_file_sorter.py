import os 
import shutil 

# 1.Get the original directory/folder where my script is saved in
source_dir = r"C:\Users\Lenovo\OneDrive\Desktop\automation_practice\Day2_File_Sorter"
print(f"Working Inside: {source_dir}")

# 2.Define the directory/folders(Images,Documents,...) and file extensions(.txt,.png) to be created in the original folder/directory
file_types = {"Images":[".jpg",".png",".gif",".jpeg"],
              "Documents":[".pdf",".docx",".txt",".xlsx"],
              "Videos":[".mp4",".mkv",".avi"],
              "Music":[".mp3",".wav"]}

# 3.Create the folders(Images,Documents,...) in 2 with their paths 
for folder in file_types.keys():
    folder_path = os.path.join(source_dir,folder)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"'{folder}' folder created!")

# 4.Create a folder for files/folders that are not originally defined in 2
uncat_file_path = os.path.join(source_dir, "Uncategorized") 
if not os.path.exists(uncat_file_path):
    os.mkdir(uncat_file_path)
    print("Uncategorized folder created!")

for file_name in os.listdir(source_dir):
    file_path = os.path.join(source_dir,file_name)
    if os.path.isdir(file_path):
        continue
    file_ext = os.path.splitext(file_name)[1].lower()
    moved = False
    for category, extensions in file_types.items():
        if file_ext in extensions:
            dest_path = os.path.join(source_dir,category,file_name)
            shutil.move(file_path,dest_path)
            print(f"{file_name} moved to {category}")
            moved = True
            break
    if not moved:
        shutil.move(file_path,os.path.join(uncat_file_path,file_name))
        print(f"{file_name} moved to Uncategorized!")
