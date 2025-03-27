"""
LangGraph-specific resources for the MCP server.
This module contains resources for accessing LangGraph documentation.
"""
import logging
from app.config import DOCS_FILE_PATH
from app.utils.logging_utils import setup_logger, log_resource_access

# Set up logger
logger = setup_logger("langgraph_resources", level=logging.INFO)

def register_langgraph_resources(mcp):
    """
    Register LangGraph-specific resources with the MCP server.
    
    Args:
        mcp: The MCP server instance
    """
    logger.info("Registering LangGraph resources")
    # Register the LangGraph documentation resource
    mcp.resource("docs://langgraph/full")(get_all_langgraph_docs)

def get_all_langgraph_docs() -> str:
    """
    Get all the LangGraph documentation. Returns the contents of the file llms_full.txt,
    which contains a curated set of LangGraph documentation (~300k tokens). This is useful
    for a comprehensive response to questions about LangGraph.

    Args: None

    Returns:
        str: The contents of the LangGraph documentation
    """
    resource_uri = "docs://langgraph/full"
    log_resource_access(logger, resource_uri)
    
    logger.info(f"Reading documentation from: {DOCS_FILE_PATH}")
    try:
        with open(DOCS_FILE_PATH, 'r') as file:
            content = file.read()
            logger.info(f"Successfully read documentation ({len(content)} characters)")
            return content
    except Exception as e:
        error_msg = f"Error reading documentation file: {str(e)}"
        logger.error(error_msg)
        return error_msg