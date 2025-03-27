# LangGraph MCP Server

A clean, modular implementation of a Model Context Protocol (MCP) server for LangGraph documentation.

## Architecture

This project follows a clean architecture pattern to make the MCP server more maintainable and easier to debug as more functionality is added.

### Directory Structure

```
app/
├── config.py                  # Configuration settings
├── server.py                  # Main server entry point
├── resources/                 # Resources that can be accessed by clients
│   ├── __init__.py            # Resource registration
│   └── langgraph_resources.py # LangGraph-specific resources
├── tools/                     # Tools that can be called by clients
│   ├── __init__.py            # Tool registration
│   └── langgraph_tools.py     # LangGraph-specific tools
└── utils/                     # Utility functions
    ├── __init__.py
    └── logging_utils.py       # Logging utilities
```

## Core Components

1. **Server**: The main entry point that initializes the MCP server and registers all tools and resources.
2. **Config**: Central location for all configuration settings.
3. **Tools**: Functions that can be called by clients to perform specific tasks.
4. **Resources**: Data sources that can be accessed by clients.
5. **Utils**: Utility functions used throughout the application.

## Adding New Functionality

### Adding a New Tool

1. Create a new file in the `app/tools/` directory (e.g., `weather_tools.py`).
2. Define your tool functions in this file.
3. Create a registration function (e.g., `register_weather_tools`).
4. Import and call this registration function in `app/tools/__init__.py`.

Example:

```python
# app/tools/weather_tools.py
def register_weather_tools(mcp):
    mcp.tool()(get_weather)

def get_weather(city: str):
    """Get weather for a city"""
    # Implementation
    return f"Weather for {city}: Sunny, 75°F"

# app/tools/__init__.py
from app.tools.langgraph_tools import register_langgraph_tools
from app.tools.weather_tools import register_weather_tools

def register_tools(mcp):
    register_langgraph_tools(mcp)
    register_weather_tools(mcp)
```

### Adding a New Resource

1. Create a new file in the `app/resources/` directory (e.g., `weather_resources.py`).
2. Define your resource functions in this file.
3. Create a registration function (e.g., `register_weather_resources`).
4. Import and call this registration function in `app/resources/__init__.py`.

Example:

```python
# app/resources/weather_resources.py
def register_weather_resources(mcp):
    mcp.resource("weather://forecast")(get_weather_forecast)

def get_weather_forecast():
    """Get weather forecast"""
    # Implementation
    return "5-day weather forecast data"

# app/resources/__init__.py
from app.resources.langgraph_resources import register_langgraph_resources
from app.resources.weather_resources import register_weather_resources

def register_resources(mcp):
    register_langgraph_resources(mcp)
    register_weather_resources(mcp)
```

## Running the Server

To run the server:

```bash
python -m app.server
```

## Benefits of This Architecture

1. **Modularity**: Each component has a single responsibility.
2. **Extensibility**: Easy to add new tools and resources without modifying existing code.
3. **Maintainability**: Organized structure makes debugging easier.
4. **Scalability**: Can handle growth as more functionality is added.
5. **Testability**: Components can be tested in isolation.