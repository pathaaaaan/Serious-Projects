import os
import shutil

directory = os.path.join(os.path.expanduser("~"), "Documents/docs pdf")

extensions = {
    ".jpg" : "Images",
    ".jpeg" : "Images",
    ".gif" : "Images",
    ".png" : "Images",
    ".mp4" : "Videos",
    ".mov" : "Videos",
    ".pdf" : "Documents",
    ".txt" : "Documents",
    ".doc" : "Documents",
    ".docx" : "Documents",
    ".xls" : "Documents",
    ".xlsx" : "Documents",
    ".mp3" : "Audio",
    ".wav" : "Audio"
}

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower()

        if extension in extensions:
            folder_name = extensions[extension]

            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            destination_path = os.path.join(folder_path, filename)
            shutil.move(file_path, destination_path)

            print(f"Moved {filename} to {folder_name} folder.")
        else:
            print(f"Skipped {filename}. Unknown file extenion.")
    else:
        print(f"Skipped {filename}. File is a directory.")

print("File Organization completed.")

