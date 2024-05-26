import sys
from file_organizer.file_sorter import sort_files

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python organize_folder.py <folder_path>")
        sys.exit(1)

    # Get the folder path from the command line arguments
    folder_path = sys.argv[1]

    # Call the sort_files function to organize the specified folder
    sort_files(folder_path)
    print(f"Organized folder: {folder_path}")

if __name__ == "__main__":
    main()
