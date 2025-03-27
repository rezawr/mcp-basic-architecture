"""
Example script demonstrating how to extend the MCP server with new tools and resources.
This script shows how to add the weather tools and resources to the MCP server.
"""
from app.server import create_server
from app.tools.weather_tools import register_weather_tools
from app.resources.weather_resources import register_weather_resources

def extend_mcp_server():
    """
    Create an MCP server and extend it with additional tools and resources.
    
    Returns:
        The extended MCP server instance
    """
    # Create the base MCP server
    mcp = create_server()
    
    # Extend with additional tools and resources
    print("Extending MCP server with weather tools and resources...")
    
    # Register weather tools
    register_weather_tools(mcp)
    
    # Register weather resources
    register_weather_resources(mcp)
    
    print("MCP server extension complete")
    return mcp

if __name__ == "__main__":
    # Create and extend the MCP server
    extended_mcp = extend_mcp_server()
    
    # Run the extended server
    print("Running extended MCP server...")
    extended_mcp.run(transport='stdio')