# Running Ollama and Langflow with Docker

This guide will help you get Ollama and LangFlow up and running using Docker and Docker Compose.

## Prerequisites

- Docker
- Docker Compose

## Run the Docker containers

1. Clone the Hackathon repository:

   ```sh
   git clone https://github.com/dkvorgbe/ALU-x-Meta-AI-Hackathon-2024.git
   ```

2. Navigate to the `docker_example` directory:

   ```sh
   cd docker_example
   ```

3. Run the Docker Compose file:

   ```sh
   docker compose up
   ```

LangFlow will now be accessible at [http://localhost:7860/](http://localhost:7860/).
Llama 3 via Ollama will now be available at [http://localhost:11434/](http://localhost:11434/).

## Docker Compose Configuration

The Docker Compose configuration spins up three services: `langflow`, `postgres`, and `ollama`.

## Install Llama 3 model in your ollama container

1. Open a new terminal tab and access the terminal of your ollama docker container from your host machine:

   ```sh
   docker exec -it ollama /bin/bash
   ```

2. Install download and run the Llama3 model

   ```sh
   ollama run llama3
   ```

