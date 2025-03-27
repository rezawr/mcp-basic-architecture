"""
Resources module for the MCP server.
This module contains all the resources that can be accessed by the client.
"""
from app.resources.langgraph_resources import register_langgraph_resources
from app.resources.weather_resources import register_weather_resources

def register_resources(mcp):
    """
    Register all resources with the MCP server.
    
    Args:
        mcp: The MCP server instance
    """
    # Register resources from different modules
    register_langgraph_resources(mcp)
    register_weather_resources(mcp)
    
    # Add more resource registrations here as needed
    # Example: register_weather_resources(mcp)
    # Example: register_database_resources(mcp)