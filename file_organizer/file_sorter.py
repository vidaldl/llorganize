import os
import shutil

# Define the base directory for sorting
SORTING_RULES = {
    'Pictures': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt']
}

def sort_files(folder_path):
    # Helper function to move files to the destination folder
    def move_file(file_path, destination_folder):
        os.makedirs(destination_folder, exist_ok=True)  # Create the folder if it doesn't exist
        destination_path = os.path.join(destination_folder, os.path.basename(file_path))
        if not os.path.exists(destination_path):
            try:
                shutil.move(file_path, destination_path)  # Move the file
                print(f"Moved file: {file_path} to {destination_folder}")
            except FileNotFoundError as e:
                print(f"Error moving file: {e}")

    # Walk through all files in the given folder
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file_path)[1].lower()
            file_name = os.path.basename(file_path)

            # Check each file against the sorting rules
            for folder, rules in SORTING_RULES.items():
                if file_extension in rules or any(rule in file_name for rule in rules):
                    move_file(file_path, os.path.join(folder_path, folder))
                    break
            else:
                # If no rule matches, move the file to the 'Other' folder
                move_file(file_path, os.path.join(folder_path, 'Other'))

if __name__ == "__main__":
    # Prompt user to enter the folder path
    folder_to_sort = input("Enter the path of the folder to sort: ")
    if os.path.exists(folder_to_sort):
        sort_files(folder_to_sort)  # Sort the files in the specified folder
    else:
        print("Folder does not exist.")
