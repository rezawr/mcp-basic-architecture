"""
Weather-specific tools for the MCP server.
This module contains tools for retrieving weather information.
"""
import logging
import json
from typing import Optional
from app.utils.logging_utils import setup_logger, log_tool_call

# Set up logger
logger = setup_logger("weather_tools", level=logging.INFO)

def register_weather_tools(mcp):
    """
    Register weather-specific tools with the MCP server.
    
    Args:
        mcp: The MCP server instance
    """
    logger.info("Registering Weather tools")
    # Register the weather tools
    mcp.tool()(get_weather)
    mcp.tool()(get_forecast)

def get_weather(city: str, country: Optional[str] = None):
    """
    Get current weather for a city.
    
    Args:
        city (str): The city to get weather for
        country (Optional[str]): The country code (optional)

    Returns:
        str: Current weather information for the specified city
    """
    location = f"{city}, {country}" if country else city
    log_tool_call(logger, "get_weather", {"city": city, "country": country})
    
    logger.info(f"Getting weather for: {location}")
    
    # This would typically call a weather API
    # For demonstration purposes, we're returning mock data
    weather_data = {
        "location": location,
        "temperature": 72,
        "condition": "Sunny",
        "humidity": 45,
        "wind_speed": 8
    }
    
    logger.info(f"Retrieved weather data for {location}")
    return json.dumps(weather_data, indent=2)

def get_forecast(city: str, days: int = 5, country: Optional[str] = None):
    """
    Get weather forecast for a city.
    
    Args:
        city (str): The city to get forecast for
        days (int): Number of days for the forecast (default: 5)
        country (Optional[str]): The country code (optional)

    Returns:
        str: Weather forecast for the specified city and number of days
    """
    location = f"{city}, {country}" if country else city
    log_tool_call(logger, "get_forecast", {"city": city, "days": days, "country": country})
    
    logger.info(f"Getting {days}-day forecast for: {location}")
    
    # This would typically call a weather API
    # For demonstration purposes, we're returning mock data
    forecast_data = {
        "location": location,
        "days": days,
        "forecast": [
            {
                "day": 1,
                "temperature": 72,
                "condition": "Sunny"
            },
            {
                "day": 2,
                "temperature": 68,
                "condition": "Partly Cloudy"
            },
            {
                "day": 3,
                "temperature": 65,
                "condition": "Cloudy"
            },
            {
                "day": 4,
                "temperature": 70,
                "condition": "Sunny"
            },
            {
                "day": 5,
                "temperature": 75,
                "condition": "Sunny"
            }
        ]
    }
    
    logger.info(f"Retrieved {days}-day forecast for {location}")
    return json.dumps(forecast_data, indent=2)