import os
import glob

# Define the folder path where you want to delete .xml files
folder_path = '.'

# Use glob to get a list of all .xml files in the folder
xml_files = glob.glob(os.path.join(folder_path, '*.xml'))

# Loop through the list of .xml files and delete them
for xml_file in xml_files:
    try:
        os.remove(xml_file)
        print(f"Deleted: {xml_file}")
    except OSError as e:
        print(f"Error deleting {xml_file}: {e}")

print("Deletion complete.")
