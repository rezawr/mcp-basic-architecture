"""
Configuration settings for the MCP server.
This file contains all the configuration variables used throughout the application.
"""

# Server name
SERVER_NAME = "LangGraph-Docs-MCP-Server"

# Define common path to the repo locally
PATH = "/mnt/c/Users/user/OneDrive/Documents/work/python/mcp-learn/"

# Vector store settings
EMBEDDING_MODEL = "text-embedding-3-large"
VECTOR_STORE_PATH = PATH + "sklearn_vectorstore.parquet"
RETRIEVER_K = 3

# Documentation settings
DOCS_FILE_PATH = PATH + "llms_full.txt"