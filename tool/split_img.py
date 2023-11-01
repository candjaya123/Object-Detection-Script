import os
import shutil
import argparse

def distribute_images(source_folder, destination_folders):
    # Create destination folders if they don't exist
    for folder in destination_folders:
        os.makedirs(folder, exist_ok=True)

    # List all image files in the source folder
    image_files = [file for file in os.listdir(source_folder) if file.startswith("frame_")]

    # Sort the image files by their numerical suffix
    image_files.sort(key=lambda x: int(x.split("_")[1]))

    # Distribute the images alternately into the destination folders
    for i, image_file in enumerate(image_files):
        dest_folder = destination_folders[i % 5]  # Alternate distribution
        source_path = os.path.join(source_folder, image_file)
        dest_path = os.path.join(dest_folder, image_file)
        shutil.copy(source_path, dest_path)

    print("Images distributed to folders successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Distribute images into 5 folders.")
    parser.add_argument("source_folder", help="Path to the source folder containing images.")
    args = parser.parse_args()

    source_folder = args.source_folder
    destination_folders = ["folder1", "folder2", "folder3", "folder4", "folder5"]

    distribute_images(source_folder, destination_folders)
