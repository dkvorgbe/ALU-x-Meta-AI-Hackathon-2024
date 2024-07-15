# ALU x Meta AI Hackathon - Lab
Welcome to companion codebase to the opening lab session for the ALU AI Hackathon in partnership with Meta.
This lab aims to get you up and running with some of the basic tools required to develop LLM-powered applications.

### Llama 3 use
Meta's Llama 3 is the most capable openly available Large language Model. The Hackathon requires participants to use Llama 3 to power some of their application's functionality. The Llama 3 model....

After successfully setting up an example in this codebase, you will be able to:
1. Serve Llama 3 models locally (subject to system specifications), using Ollama
2. Design and run flows that orchestrate complex behaviours with LLMs, using Langflow

## Overview
This codebase uses Ollama and Langflow to serve LLMs and orchestrate complex behaviour with them respectively. 

1. [Ollama](http://ollama.com):
    Ollama simplifies the hosting and serving of language models locally for the ease of development. Typically,  It offers quantized versions of of popular models, reducing the system requirements needed to run models.

2. [Langflow](https://langflow.com)
    Langflow simplifies LLM orchestration with a powerful and simple to use user interface that allows you to design and run complex interactions between models, vector stores, and many typical components required to build llm-powered applications.

Note that Ollama and Langflow are only an example each of the numerous ways to serve language models, and to achieve orchestration respectively. You are free to use any tools or methods of your choosing for your project.


### System requirements
Large language Models generally require powerful GPUs to run inference in production applications. However, smaller models can be sucesssfully run on consumer CPUs. Still, Ollama's minimum system requirements may exceed your computer's capabilities. For this lab, Ollama has been sucessfully tested on a 2021 M1 Macbook Pro with 16Gb of RAM and 8 CPU cores.

### Accessing a remote Ollama instance
For users who are not able to run the Llama 3 model locally via Ollama, a server runinng Ollama with a Llama 3 inference model and a xxxxx embedding model have been made available. Reach out to the faciliatator for the URLs.

## Getting started

### Install and run Ollama 
This step is only necessary if you are running the Llama 3 model locally via Ollama. 

1. Download and install Ollama for your system
2. Open Ollama
3. Download a model (Llama3:7B receommended)
3. Run the model
4. Interact with the model via your CLI or make an HTTP request

Once you have Ollama running locally, you can select your preferred setup below to continue:

### Setup choices

The codebase offers 3 different setup choices for running Ollama and Langflow. You only have to select your preferred method out of:

1. [Python - Virtualenv](https://link.to.python.com)
2. [Python - Docker](https://link.to.python.com):
3. [Javascript Docker](https://link.to.python.com)



