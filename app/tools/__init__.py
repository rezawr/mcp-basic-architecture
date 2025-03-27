"""
Tools module for the MCP server.
This module contains all the tools that can be called by the client.
"""
from app.tools.langgraph_tools import register_langgraph_tools
from app.tools.weather_tools import register_weather_tools

def register_tools(mcp):
    """
    Register all tools with the MCP server.
    
    Args:
        mcp: The MCP server instance
    """
    # Register tools from different modules
    register_langgraph_tools(mcp)
    register_weather_tools(mcp)