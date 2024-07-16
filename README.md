# ALU x Meta AI Hackathon - Lab
Welcome to companion codebase to the opening lab session for the ALU AI Hackathon in partnership with Meta.
This lab aims to get you up and running with some of the basic tools required to develop LLM-powered applications.

### Llama 3 use
Meta's Llama 3 is the most capable openly available Large Language Model. The Hackathon requires participants to use Llama 3 to power some of their application's functionality.

After successfully setting up the examples in this codebase, you will be able to:
1. Serve Llama 3 models locally (subject to system specifications), using [Ollama](https://github.com/ollama/ollama)
2. Design and run flows that orchestrate complex behaviours with LLMs, using [Langflow](https://github.com/langflow-ai/langflow)

## Overview
This codebase uses Ollama to serve Llama3 and Langflow to orchestrate complex behaviour. 

1. [Ollama](https://github.com/ollama/ollama):
    Ollama simplifies the hosting and serving of language models locally for the ease of development. It offers quantized versions of of popular models, lowering the system requirements needed to run them.

2. [Langflow](https://github.com/langflow-ai/langflow)
    Langflow simplifies LLM orchestration with a powerful and simple to use user interface. It allows you to design and run complex interactions between models, vector stores, and many typical components required to build llm-powered applications.

Note that Ollama and Langflow are only an example each of the numerous ways to serve language models, and to achieve orchestration. You are free to use any tools or methods of your choosing for your project.


### System requirements
Large language Models generally require powerful GPUs to run inference in production applications. Smaller models can be sucesssfully run on consumer CPUs. Still, Ollama's minimum system requirements may exceed your computer's capabilities. For this lab, Ollama has been sucessfully tested on a 2021 M1 Macbook Pro with 16Gb of RAM and 8 CPU cores.

### Accessing a remote Ollama instance
For users who are not able to run the Llama 3 model locally via Ollama, a server runinng Ollama with a Llama 3 inference model and an embedding model will be made available during the hackathon. Reach out to the faciliatator for the URLs.

## Getting started

### Setup choices

The codebase offers 2 different setup choices for running Ollama and Langflow. You only have to select your preferred method or use it as reference

1. [Python - virtualenv example](https://github.com/dkvorgbe/ALU-x-Meta-AI-Hackathon-2024/tree/main/virtualenv_example)
2. [Python - docker example](https://github.com/dkvorgbe/ALU-x-Meta-AI-Hackathon-2024/tree/main/docker_example):


