from langflow.load import run_flow_from_json
import os

TWEAKS = {
  "OllamaEmbeddings-YWfjV": {
    "base_url": "http://localhost:11434",
    "model": "mxbai-embed-large",
    "temperature": 0.1
  },
  "ChatInput-THQC8": {
    "files": "",
    "input_value": "What programs does the university offer?",
    "sender": "User",
    "sender_name": "User",
    "session_id": "",
    "store_message": True
  },
  "Prompt-3BPeu": {
    "template": "You are an expert at reading contextual information and providing answers based on the context. \nDo not make things up. Only use the context provided to answer the question. If there is not enough information about the context let the user know.\nKeep your answers short, under 3 senteces.\n\nYou are provided with the following:\n\nContext: {context}\n\nQuestion: {question}\n\n\n",
    "context": "",
    "question": ""
  },
  "Chroma-sip28": {
    "allow_duplicates": False,
    "chroma_server_cors_allow_origins": "",
    "chroma_server_grpc_port": None,
    "chroma_server_host": "",
    "chroma_server_http_port": None,
    "chroma_server_ssl_enabled": False,
    "collection_name": "pdf_chat",
    "limit": None,
    "number_of_results": 10,
    "persist_directory": "chroma_db",
    "search_query": "",
    "search_type": "Similarity"
  },
  "ParseData-2ja7A": {
    "sep": "\n",
    "template": "{text}"
  },
  "ChatOutput-gk0BM": {
    "data_template": "{text}",
    "input_value": "",
    "sender": "Machine",
    "sender_name": "AI",
    "session_id": "",
    "store_message": True
  },
  "OllamaModel-F5mAo": {
    "base_url": "http://localhost:11434",
    "format": "",
    "input_value": "",
    "metadata": {},
    "mirostat": "Disabled",
    "mirostat_eta": None,
    "mirostat_tau": None,
    "model": "llama3:latest",
    "num_ctx": None,
    "num_gpu": None,
    "num_thread": None,
    "repeat_last_n": None,
    "repeat_penalty": None,
    "stop_tokens": "",
    "stream": False,
    "system": "",
    "system_message": "",
    "tags": "",
    "temperature": 0.2,
    "template": "",
    "tfs_z": None,
    "timeout": None,
    "top_k": None,
    "top_p": None,
    "verbose": False
  }
}

flow_path = os.path.join(os.path.dirname(__file__), "flows/chat_with_vector_response_as_context.json")

result = run_flow_from_json(flow=flow_path,
                            input_value="message",
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)

llm_response = result[0].outputs[0].results

print(llm_response)