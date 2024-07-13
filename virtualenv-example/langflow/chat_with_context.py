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
    "input_value": "How many hours can a hackathon last?",
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
  }
}

flow_path = os.path.join(os.path.dirname(__file__), "flows/chat_with_vector_response_as_context.json")

result = run_flow_from_json(flow=flow_path,
                            input_value="how long should a hackathon be run?",
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)

from pprint import pprint
pprint(result)