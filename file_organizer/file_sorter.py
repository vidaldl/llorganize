import os
import shutil

def move_file_to_folder(source_path, destination_folder):
    """Moves a file to the specified destination folder, creating the folder if it doesn't exist."""
    os.makedirs(destination_folder, exist_ok=True)  # Ensure the destination folder exists
    destination_path = os.path.join(destination_folder, os.path.basename(source_path))
    if not os.path.exists(destination_path):  # Avoid overwriting existing files
        try:
            shutil.move(source_path, destination_path)  # Attempt to move the file
            print(f"Moved file: {source_path} to {destination_folder}")
        except FileNotFoundError as e:
            print(f"Error moving file: {e}")

def sort_files(folder_path):
    """Sorts files in the specified folder based on file extensions or file name keywords."""
    # Walk through all files in the folder
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file_path)[1].lower()  # Extract file extension
            file_name = os.path.basename(file_path).lower()  # Extract the base name of the file

            # Define file paths for categories
            pictures_folder = os.path.join(folder_path, 'Pictures')
            documents_folder = os.path.join(folder_path, 'Documents')
            other_folder = os.path.join(folder_path, 'Other')

            # Sorting conditions for each category
            if file_extension in ['.jpg', '.jpeg', '.png', '.gif']:
                move_file_to_folder(file_path, pictures_folder)
            elif file_extension in ['.pdf', '.docx', '.txt']:
                move_file_to_folder(file_path, documents_folder)
            else:
                move_file_to_folder(file_path, other_folder)

if __name__ == "__main__":
    folder_to_sort = input("Enter the path of the folder to sort: ")
    if os.path.exists(folder_to_sort):
        sort_files_in_folder(folder_to_sort)
    else:
        print("Folder does not exist.")
