# Running Ollama and Langflow with Docker

This guide will help you get Ollama and LangFlow up and running using a Python virtual environment.

## Prerequisites

- Python3.1
- Virtualenv

## Download Ollama and Llam3 Model

1. Visit [ollama.com](https://ollama.com/)
2. Download and install Ollama
3. Open a terminal window and run 
    ```sh
    ollama run llama3
    ```

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

1. Run the example 
   ```sh
   ```

