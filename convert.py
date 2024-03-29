import os
import pyvips
import subprocess
from tqdm import tqdm  # Import tqdm for progress bars

# Function to convert HEIC to JPG
def convert_heic_to_jpg(file_path):
    # Open the HEIC image using pyvips
    im = pyvips.Image.new_from_file(file_path, access="sequential")
    # Define the output JPG path by replacing the extension
    jpg_path = os.path.splitext(file_path)[0] + ".jpg"
    # Write the image to the JPG file
    im.write_to_file(jpg_path, Q=90)
    return jpg_path

# Function to convert MOV to MP4
def convert_mov_to_mp4(file_path):
    # Define the output MP4 path by replacing the extension
    mp4_path = os.path.splitext(file_path)[0] + ".mp4"
    # Use subprocess to run ffmpeg command to convert MOV to MP4
    subprocess.run(['ffmpeg', '-i', file_path, '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-c:a', 'aac', '-b:a', '160k', '-movflags', 'faststart', mp4_path], capture_output=True)
    return mp4_path

# Function to remove original file after conversion
def remove_original(file_path):
    os.remove(file_path)

# Main function to convert media files
def convert_media_files(folder_path):
    # Walk through the directory tree
    for root, dirs, files in os.walk(folder_path):
        # For each file in the current directory
        for file in tqdm(files, desc="Converting files"):  # tqdm for progress bar
            file_path = os.path.join(root, file)
            file_ext = os.path.splitext(file)[1].lower()
            # Check file extension
            if file_ext == ".heic":
                tqdm.write("Converting HEIC to JPG: " + file_path)
                # Convert HEIC to JPG
                converted_path = convert_heic_to_jpg(file_path)
                tqdm.write("Converted to: " + converted_path)
                # Remove original HEIC file
                remove_original(file_path)
                tqdm.write("Removed original: " + file_path)
            elif file_ext == ".mov":
                tqdm.write("Converting MOV to MP4: " + file_path)
                # Convert MOV to MP4
                converted_path = convert_mov_to_mp4(file_path)
                tqdm.write("Converted to: " + converted_path)
                # Remove original MOV file
                remove_original(file_path)
                tqdm.write("Removed original: " + file_path)

def main():
    # Specify the folder containing the files
    folder_path = "/home/appleboblin/Downloads/covhe/"

    # convert the files
    convert_media_files(folder_path)

if __name__ == '__main__':
    main()