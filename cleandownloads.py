import os
import shutil

# Define the path to the Downloads folder
downloads_folder = os.path.expanduser("~/Downloads")

# Create a dictionary to map file extensions to folder names
filetype_to_folder = {
    ".pdf": "PDFs",
    ".jpg": "Images",
    ".png": "Images",
    ".docx": "Documents",
    ".xlsx": "Documents",
    ".exe": "Exe's"
    # Add more extensions and corresponding folder names as needed
}

# Iterate over files in the Downloads folder
for filename in os.listdir(downloads_folder):
    filepath = os.path.join(downloads_folder, filename)
    if os.path.isfile(filepath):
        # Get the file extension
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        # Get the corresponding folder name
        folder_name = filetype_to_folder.get(extension, "Other")

        # Create the folder if it doesn't exist
        folder_path = os.path.join(downloads_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        # Move the file to the appropriate folder
        new_filepath = os.path.join(folder_path, filename)
        shutil.move(filepath, new_filepath)
        print(f"Moved {filename} to {folder_name} folder.")

print("Files in Downloads folder have been organized by filetype into folders.")
