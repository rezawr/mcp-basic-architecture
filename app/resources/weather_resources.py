"""
Weather-specific resources for the MCP server.
This module contains resources for accessing weather information.
"""
import logging
import json
from app.utils.logging_utils import setup_logger, log_resource_access

# Set up logger
logger = setup_logger("weather_resources", level=logging.INFO)

def register_weather_resources(mcp):
    """
    Register weather-specific resources with the MCP server.
    
    Args:
        mcp: The MCP server instance
    """
    logger.info("Registering Weather resources")
    # Register the weather resources
    mcp.resource("weather://locations/popular")(get_popular_locations)
    mcp.resource("weather://info/units")(get_weather_units)

def get_popular_locations() -> str:
    """
    Get a list of popular locations for weather queries.

    Args: None

    Returns:
        str: JSON string containing popular locations
    """
    resource_uri = "weather://locations/popular"
    log_resource_access(logger, resource_uri)
    
    logger.info("Retrieving popular weather locations")
    
    # This would typically come from a database or API
    # For demonstration purposes, we're returning mock data
    locations = [
        {"city": "New York", "country": "US"},
        {"city": "London", "country": "UK"},
        {"city": "Tokyo", "country": "JP"},
        {"city": "Sydney", "country": "AU"},
        {"city": "Paris", "country": "FR"},
        {"city": "Berlin", "country": "DE"},
        {"city": "Cairo", "country": "EG"},
        {"city": "Rio de Janeiro", "country": "BR"},
        {"city": "Moscow", "country": "RU"},
        {"city": "Beijing", "country": "CN"}
    ]
    
    logger.info(f"Retrieved {len(locations)} popular locations")
    return json.dumps(locations, indent=2)

def get_weather_units() -> str:
    """
    Get information about weather units used in the API.

    Args: None

    Returns:
        str: JSON string containing weather unit information
    """
    resource_uri = "weather://info/units"
    log_resource_access(logger, resource_uri)
    
    logger.info("Retrieving weather unit information")
    
    # Static information about units
    units_info = {
        "temperature": {
            "default": "Fahrenheit",
            "available": ["Fahrenheit", "Celsius", "Kelvin"]
        },
        "wind_speed": {
            "default": "mph",
            "available": ["mph", "km/h", "m/s", "knots"]
        },
        "pressure": {
            "default": "inHg",
            "available": ["inHg", "mbar", "hPa"]
        },
        "precipitation": {
            "default": "inches",
            "available": ["inches", "mm"]
        }
    }
    
    logger.info("Retrieved weather unit information")
    return json.dumps(units_info, indent=2)