import os
import shutil
import sys

def copy_files(source_dir, dest_dir):
    try:
        # Iterate over items in the source directory
        for item in os.listdir(source_dir):
            item_path = os.path.join(source_dir, item)
            if os.path.isdir(item_path):
                # Recursively call the function if item is a directory
                copy_files(item_path, dest_dir)
            elif os.path.isfile(item_path):
                # Get the file extension
                _, extension = os.path.splitext(item)
                # Create subdirectory based on file extension
                subdirectory = os.path.join(dest_dir, extension[1:])
                os.makedirs(subdirectory, exist_ok=True)
                # Copy file to corresponding subdirectory
                shutil.copy2(item_path, subdirectory)
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Parsing command line arguments
    if len(sys.argv) < 2:
        print("Usage: python script.py source_dir [dest_dir]")
        sys.exit(1)
    
    source_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"
    
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        sys.exit(1)
    
    try:
        # Call function to copy files
        copy_files(source_dir, dest_dir)
        print("Files copied successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
