# Running Ollama and Langflow with Python Virtualenv

This guide will help you get Ollama and LangFlow up and running using a Python virtual environment.

## Prerequisites

- Python3.1
- Virtualenv

## Download Ollama and Llam3 Model

1. Visit [ollama.com](https://ollama.com/)
2. Download and install Ollama
3. Open a terminal window and download the llama3 model

    ```sh
    ollama run llama3
    ```

Ensure that Llama3 is working before you proceed.

## Create a virtual environment

1. Clone the Hackathon repository:

   ```sh
   git clone https://github.com/dkvorgbe/ALU-x-Meta-AI-Hackathon-2024.git
   ```

2. Navigate to the `virtualenv_example` directory:

   ```sh
   cd virtualenv_example
   ```

3. Create a new virtualenv:

   ```sh
   python3.1 -m venv venv
   ```

3. Activate the virtualenv:

   ```sh
   source env/bin/activate
   ```

4. Install requirements

    ```sh
    pip install -r requirements.txt
    ```

5. Run langflow

    ```sh
    python -m langflow run
    ```

LangFlow will now be accessible at [http://localhost:7860/](http://localhost:7860/).
Llama 3 via Ollama will now be available at [http://localhost:11434/](http://localhost:11434/).

## Run the example apps

### Ollama - Langflow

Start the langflow service:

```sh
python -m langflow run
```

The examples enable you to:
1. Split a pdf file and store its contents in a vector database
2. Ask Llama3 any questions about the context of the file

The order of runs matters. You  must first store the files contents in a vector store and then you can chat with the context.

You must be in the `virtualenv_example/langflow` directory for the following:

 ```sh
   cd virtualenv_example/langflow
 ```

1. Split file contents and store in a vector database

   ```sh
   python store_file_as_vector.py
   ```

2. Chat with pdf file context

   ```sh
   python chat_with_context.py
   ```

Navigate to the `virtualenv_example/ollama` directory for the following:

 ```sh
   cd virtualenv_example/ollama
 ```

3. Prompt Llama3 with python

```sh
python simple_prompt.py
```

