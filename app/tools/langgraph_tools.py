"""
LangGraph-specific tools for the MCP server.
This module contains tools for interacting with LangGraph documentation.
"""
import logging
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import SKLearnVectorStore
from app.config import EMBEDDING_MODEL, VECTOR_STORE_PATH, RETRIEVER_K
from app.utils.logging_utils import setup_logger, log_tool_call

# Set up logger
logger = setup_logger("langgraph_tools", level=logging.INFO)

def register_langgraph_tools(mcp):
    """
    Register LangGraph-specific tools with the MCP server.
    
    Args:
        mcp: The MCP server instance
    """
    logger.info("Registering LangGraph tools")
    # Register the LangGraph query tool
    mcp.tool()(langgraph_query_tool)

def langgraph_query_tool(query: str):
    """
    Query the LangGraph documentation using a retriever.
    
    Args:
        query (str): The query to search the documentation with

    Returns:
        str: A str of the retrieved documents
    """
    log_tool_call(logger, "langgraph_query_tool", {"query": query})
    
    logger.info(f"Creating retriever with model: {EMBEDDING_MODEL}")
    retriever = SKLearnVectorStore(
        embedding=OpenAIEmbeddings(model=EMBEDDING_MODEL),
        persist_path=VECTOR_STORE_PATH,
        serializer="parquet").as_retriever(search_kwargs={"k": RETRIEVER_K}
        )

    logger.info(f"Querying with: '{query}'")
    relevant_docs = retriever.invoke(query)
    logger.info(f"Retrieved {len(relevant_docs)} relevant documents")
    
    formatted_context = "\n\n".join([f"==DOCUMENT {i+1}==\n{doc.page_content}" for i, doc in enumerate(relevant_docs)])
    return formatted_context