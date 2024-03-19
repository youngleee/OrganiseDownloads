import os
import time
import shutil

def move_old_files(directory_path, target_folder):
    # Get the current timestamp
    current_time = time.time()

    # Define the threshold (6 months = 180 days)
    threshold_seconds = 180 * 24 * 60 * 60

    # Create the target folder if it doesn't exist
    os.makedirs(target_folder, exist_ok=True)

    # Iterate over files in the directory
    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)
        if os.path.isfile(filepath):
            # Get the file's last access time
            last_access_time = os.path.getatime(filepath)

            # Calculate the time difference in seconds
            time_difference = current_time - last_access_time

            # Check if the file is older than 6 months
            if time_difference > threshold_seconds:
                # Move the file to the target folder
                new_filepath = os.path.join(target_folder, filename)
                shutil.move(filepath, new_filepath)
                print(f"Moved {filename} to {target_folder}.")

    print(f"Files older than 6 months have been moved to {target_folder}.")

# Define the directory path (Downloads folder in this case)
downloads_folder = os.path.expanduser("~/Downloads")

# Define the target folder
target_folder = os.path.join(downloads_folder, "old")

# Call the function to move old files
move_old_files(downloads_folder, target_folder)
