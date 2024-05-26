# Overview
 This project was a real challenge for me. I did a lot of research concerning LLMs and came up with a cool little python script that talks to a local Llama3 instance.
 The coolest part about this project is that you can tell Llama3 to organize a folder and it will trigger a python script that will do just that for you. 

 It was all pretty fun to learn and work on!

 Feel free to follow the installation instructions to replicate it.
 
 

[Check out my program!](https://youtu.be/ciJgocx6fQg)

# Development Environment

I used VS Code as a code editor, Ollama running Llama3, and python in this project. I also used PostMan to test my calls to the local Ollama server.

# Useful Websites

* [Ollama](https://ollama.com/)
* [Python](https://www.w3schools.com/typescript/)
* [Ollama API Documentation](https://github.com/ollama/ollama/blob/main/docs/api.md#generate-a-completion)
* [Postman](https://www.postman.com/)


## Requirements

- Python 3.x
- Ollama
- Virtual environment (recommended)

## Installation

I recommend using your own pyenv to run this.

1. **Clone the repository:**
   ```bash
   git clone git@github.com:vidaldl/llorganize.git
   cd file_organizer
   ```

2. **Install the required libraries:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Ollama and set up Llama3**
    - macOS:
        ```bash
        brew install ollama
        ```
    - Windows:
        Download the installer from the [Ollama](https://ollama.com/) website and follow the instructions.
    - Install the Llama3 model:
        ```bash
        ollama install llama3
        ```

4. **Start the Ollama server**
   ```bash
   ollama serve
   ```

## Usage
1. **Interact with Llama3:** \
    Run the script to start a conversation with Llama3 and trigger folder organization:
    ```bash
   python scripts/interact_llama.py
   ```
   - Example interaction:
        ```makefile
        You: Hello, Llama3!
        Llama3: Hi! How can I help you today?
        You: Can you organize C:\monitored_folder?
        Llama3: Organized folder: C:\monitored_folder
        ```
