"""
Main entry point for the MCP server.
This file initializes and runs the MCP server with all registered tools and resources.
"""
import logging
from mcp.server.fastmcp import FastMCP
from app.config import SERVER_NAME
from app.tools import register_tools
from app.resources import register_resources
from app.utils.logging_utils import setup_logger

# Set up logger
logger = setup_logger("mcp_server", level=logging.INFO)

def create_server():
    """Create and configure the MCP server with all tools and resources."""
    logger.info(f"Creating MCP server: {SERVER_NAME}")
    
    # Create the MCP server instance
    mcp = FastMCP(SERVER_NAME)
    
    # Register all tools and resources
    logger.info("Registering tools...")
    register_tools(mcp)
    
    logger.info("Registering resources...")
    register_resources(mcp)
    
    logger.info("Server setup complete")
    return mcp

if __name__ == "__main__":
    # Initialize and run the server
    logger.info("Starting MCP server...")
    server = create_server()
    server.run(transport='stdio')
    logger.info("Server stopped")