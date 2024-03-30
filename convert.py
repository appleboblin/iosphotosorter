import os
import shutil
import subprocess
import pyvips

def convert_heic_to_jpg(heic_file, jpg_file):
    """
    Convert HEIC file to JPG using pyvips library.
    """
    image = pyvips.Image.new_from_file(heic_file, access="sequential")
    image.write_to_file(jpg_file)

def convert_mov_to_mp4(mov_file, mp4_file):
    """
    Convert MOV file to MP4 using ffmpeg.
    """
    # No transcode, some videos are in H.264, some in H.265. Audo are in AAC and pcm_s16le. Theres no need to change. 
    command = ["ffmpeg", "-y", "-i", mov_file, "-codec", "copy", mp4_file]
    subprocess.run(command, check=True)

def convert_files_in_folder(folder_path):
    """
    Convert HEIC files to JPG and MOV files to MP4 in a folder.
    """
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_name_no_ext, file_ext = os.path.splitext(file_name)
            if file_ext.lower() == '.heic':
                jpg_file = os.path.join(root, file_name_no_ext + '.jpg')
                convert_heic_to_jpg(file_path, jpg_file)
                print(f"Converted {file_name} to {file_name_no_ext + '.jpg'}")
                os.remove(file_path)  # Remove the original HEIC file
            elif file_ext.lower() == '.mov':
                mp4_file = os.path.join(root, file_name_no_ext + '.mp4')
                convert_mov_to_mp4(file_path, mp4_file)
                print(f"Converted {file_name} to {file_name_no_ext + '.mp4'}")
                os.remove(file_path)  # Remove the original MOV file

# Example usage:
folder_path = "/home/appleboblin/Downloads/imacphoto/"
convert_files_in_folder(folder_path)
