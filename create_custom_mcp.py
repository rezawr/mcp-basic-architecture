"""
Example script demonstrating how to create a custom MCP server from scratch.
This script shows how to create a new MCP server with custom tools and resources.
"""
import logging
from mcp.server.fastmcp import FastMCP
from app.utils.logging_utils import setup_logger, log_tool_call, log_resource_access

# Set up logger
logger = setup_logger("custom_mcp", level=logging.INFO)

def create_custom_mcp_server():
    """
    Create a custom MCP server with specialized tools and resources.
    
    Returns:
        The custom MCP server instance
    """
    # Create a new MCP server
    logger.info("Creating custom MCP server")
    mcp = FastMCP("Custom-Calculator-MCP-Server")
    
    # Register calculator tools
    logger.info("Registering calculator tools")
    
    @mcp.tool()
    def add(a: float, b: float):
        """Add two numbers."""
        log_tool_call(logger, "add", {"a": a, "b": b})
        result = a + b
        logger.info(f"Calculated {a} + {b} = {result}")
        return result
    
    @mcp.tool()
    def subtract(a: float, b: float):
        """Subtract b from a."""
        log_tool_call(logger, "subtract", {"a": a, "b": b})
        result = a - b
        logger.info(f"Calculated {a} - {b} = {result}")
        return result
    
    @mcp.tool()
    def multiply(a: float, b: float):
        """Multiply two numbers."""
        log_tool_call(logger, "multiply", {"a": a, "b": b})
        result = a * b
        logger.info(f"Calculated {a} * {b} = {result}")
        return result
    
    @mcp.tool()
    def divide(a: float, b: float):
        """Divide a by b."""
        log_tool_call(logger, "divide", {"a": a, "b": b})
        if b == 0:
            error = "Cannot divide by zero"
            logger.error(error)
            raise ValueError(error)
        result = a / b
        logger.info(f"Calculated {a} / {b} = {result}")
        return result
    
    # Register calculator resources
    logger.info("Registering calculator resources")
    
    @mcp.resource("calculator://constants")
    def get_math_constants():
        """Get common mathematical constants."""
        log_resource_access(logger, "calculator://constants")
        logger.info("Retrieving mathematical constants")
        constants = {
            "pi": 3.14159265359,
            "e": 2.71828182846,
            "golden_ratio": 1.61803398875,
            "sqrt_2": 1.41421356237,
            "sqrt_3": 1.73205080757
        }
        return constants
    
    @mcp.resource("calculator://formulas/area")
    def get_area_formulas():
        """Get common area formulas."""
        log_resource_access(logger, "calculator://formulas/area")
        logger.info("Retrieving area formulas")
        formulas = {
            "square": "side * side",
            "rectangle": "length * width",
            "circle": "pi * radius * radius",
            "triangle": "0.5 * base * height",
            "trapezoid": "0.5 * (a + b) * height"
        }
        return formulas
    
    logger.info("Custom MCP server creation complete")
    return mcp

if __name__ == "__main__":
    # Create the custom MCP server
    custom_mcp = create_custom_mcp_server()
    
    # Run the custom server
    logger.info("Running custom MCP server...")
    custom_mcp.run(transport='stdio')