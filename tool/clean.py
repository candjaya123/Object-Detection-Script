import os
import argparse

def delete_images_without_xml(base_dir):
    image_dir = base_dir
    xml_dir = base_dir

    # Get a list of image and XML files
    image_files = [file for file in os.listdir(image_dir) if file.endswith(".jpg")]  # Change the extension to match your image files
    xml_files = [file for file in os.listdir(xml_dir) if file.endswith(".xml")]  # Change the extension to match your XML files

    # Create a set of the base file names without extensions
    image_names = set(os.path.splitext(file)[0] for file in image_files)
    xml_names = set(os.path.splitext(file)[0] for file in xml_files)

    # Find image files without corresponding XML files and delete them
    for image_name in image_names:
        if image_name not in xml_names:
            image_path = os.path.join(image_dir, image_name + ".jpg")  # Change the extension to match your image files
            os.remove(image_path)
            print(f"Deleted: {image_path}")

    # Optionally, you can also delete XML files without corresponding images
    for xml_name in xml_names:
        if xml_name not in image_names:
            xml_path = os.path.join(xml_dir, xml_name + ".xml")  # Change the extension to match your XML files
            os.remove(xml_path)
            print(f"Deleted: {xml_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Delete image files without corresponding XML files.")
    parser.add_argument("directory", help="Path to the directory containing both image and XML files.")

    args = parser.parse_args()
    delete_images_without_xml(args.directory)

# python clean.py /path/to/your/data_directory
