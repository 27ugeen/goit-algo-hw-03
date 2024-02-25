from pathlib import Path
import shutil
import sys

def copy_files(source_dir, dest_dir):
    try:
        # Iterate over items in the source directory
        for item in source_dir.iterdir():
            if item.is_dir():
                # Recursively call the function if item is a directory
                copy_files(item, dest_dir)
            elif item.is_file():
                # Get the file extension
                extension = item.suffix
                # Create subdirectory based on file extension
                subdirectory = dest_dir / extension[1:]
                subdirectory.mkdir(parents=True, exist_ok=True)
                # Copy file to corresponding subdirectory
                shutil.copy2(str(item), str(subdirectory))
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Parsing command line arguments
    if len(sys.argv) < 2:
        print("Usage: python3 script.py source_dir [dest_dir]")
        print("Note: The source_dir should be the path to the source directory.")
        print("      The dest_dir (optional) should be the path to the destination directory.")
        sys.exit(1)
    
    # Get the current directory
    current_dir = Path.cwd()
    
    # Form the full path of the source directory
    source_dir = Path(sys.argv[1]).resolve()
    
    # Form the full path of the destination directory
    dest_dir = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else current_dir / "dist"
    
    if not source_dir.exists():
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
