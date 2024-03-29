import os
from datetime import datetime
import shutil

# Function to sort files into year and month folders based on creation date and make file extensions lowercase
def sort_files_by_date(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                modification_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                _, file_extension = os.path.splitext(file)
                new_filename = modification_time.strftime("%Y%m%d_%H%M%S") + file_extension.lower()

                year_folder = os.path.join(folder_path, str(modification_time.year))
                month_folder = os.path.join(year_folder, f"{modification_time.month:02d}")
                os.makedirs(month_folder, exist_ok=True)

                # Move the file to the corresponding year/month folder with the new filename
                new_file_path = os.path.join(month_folder, new_filename)
                shutil.move(file_path, new_file_path)

            except Exception as e:
                print(f"Error processing {file_path}: {e}")

def main():
    # Specify the folder containing the images
    folder_path = "/home/appleboblin/Downloads/covhe/"

    # Sort and convert files
    sort_files_by_date(folder_path)

if __name__ == '__main__':
    main()