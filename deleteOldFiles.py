import os
import time

def delete_old_files(directory_path):
    # Get the current timestamp
    current_time = time.time()

    # Iterate over files and subdirectories in the directory
    for root, dirs, files in os.walk(directory_path):
        for filename in files:
            filepath = os.path.join(root, filename)
            if os.path.isfile(filepath):
                # Get the file's last access time
                last_access_time = os.path.getatime(filepath)

                # Calculate the time difference in seconds
                time_difference = current_time - last_access_time

                # Define the threshold (1 year = 365 days)
                threshold_seconds = 365 * 24 * 60 * 60

                # Check if the file hasn't been accessed in over a year
                if time_difference > threshold_seconds:
                    # Delete the file
                    os.remove(filepath)
                    print(f"Deleted {filename} (not accessed in over a year).")

    print("Files that haven't been accessed in over a year have been deleted.")

# Define the directory path (Downloads folder in this case)
downloads_folder = os.path.expanduser("~/Downloads")

# Call the function to delete old files
delete_old_files(downloads_folder)
