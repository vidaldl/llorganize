import requests
import os
import sys

# Add the project root to the PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from file_organizer.file_sorter import sort_files

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def ask_llama(prompt):
    # Send a prompt to the Llama3 model and return the response.
    try:
        response = requests.post(OLLAMA_API_URL, json={"model": "llama3", "prompt": prompt, "stream": False})
        response.raise_for_status()
        return response.json().get("response", "No response from Llama3.")
    except requests.exceptions.RequestException as e:
        return f"Error communicating with Llama3: {e}"

def organize_folder(folder_path):
    # Sort files in the specified folder.
    sort_files(folder_path)
    return f"Organized folder: {folder_path}"

def process_command(command):
    #Process user commands and trigger folder organization if requested.
    if "organize" in command.lower():
        parts = command.split()
        for i, part in enumerate(parts):
            # Get directory after word organize
            if part.lower() == "organize" and i + 1 < len(parts):
                folder_path = parts[i + 1]
                if os.path.exists(folder_path):
                    return organize_folder(folder_path)
                else:
                    return "Folder does not exist."
    return "Sorry, I didn't understand that command."

def main():
    #Main function to start the conversation with Llama3.
    print("Starting conversation with Llama3. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = ask_llama(user_input)
        print(f"Llama3: {response}")
        command_response = process_command(user_input)
        if command_response != "Sorry, I didn't understand that command.":
            print(f"Llama3: {command_response}")

if __name__ == "__main__":
    main()
