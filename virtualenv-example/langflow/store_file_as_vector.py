from langflow.load import run_flow_from_json
import os

TWEAKS = {
  "Chroma-IN9jc": {
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
  "OllamaEmbeddings-f3xjm": {
    "base_url": "http://localhost:11434",
    "model": "mxbai-embed-large",
    "temperature": 0.1
  },
  "File-EKi71": {
    "path": os.path.join(os.path.dirname(__file__), "pdf_files/alu_overview.pdf"),
    "silent_errors": False
  },
  "RecursiveCharacterTextSplitter-VAUSI": {
    "chunk_overlap": 200,
    "chunk_size": 2000,
    "separators": [
      "."
    ]
  }
}

flow_path = os.path.join(os.path.dirname(__file__), "flows/chunk_store_file_as_vector.json")

result = run_flow_from_json(flow=flow_path,
                            input_value="message",
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)

from pprint import pprint
pprint(result)
