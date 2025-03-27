"""
Test script for the MCP server.
This script demonstrates how to use the MCP server as a client.
"""
import json
import sys
import subprocess
import time
from typing import Dict, Any

def start_mcp_server():
    """Start the MCP server in a subprocess."""
    print("Starting MCP server...")
    process = subprocess.Popen(
        [sys.executable, "-m", "app.server"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )
    # Give the server a moment to start up
    time.sleep(1)
    return process

def send_request(process, request_type: str, **kwargs) -> Dict[str, Any]:
    """
    Send a request to the MCP server.
    
    Args:
        process: The subprocess running the MCP server
        request_type: The type of request (tool or resource)
        **kwargs: Additional arguments for the request
        
    Returns:
        Dict[str, Any]: The response from the server
    """
    request = {
        "type": request_type,
        **kwargs
    }
    
    # Send the request to the server
    request_json = json.dumps(request) + "\n"
    process.stdin.write(request_json)
    process.stdin.flush()
    
    # Read the response
    response_json = process.stdout.readline().strip()
    return json.loads(response_json)

def test_langgraph_query_tool(process):
    """Test the LangGraph query tool."""
    print("\n=== Testing LangGraph Query Tool ===")
    
    response = send_request(
        process,
        request_type="tool",
        server_name="LangGraph-Docs-MCP-Server",
        tool_name="langgraph_query_tool",
        arguments={"query": "How do I create a graph?"}
    )
    
    print(f"Response status: {response.get('status', 'unknown')}")
    if response.get("status") == "success":
        # Print just the first 200 characters of the result for brevity
        result = response.get("result", "")
        print(f"Result preview: {result[:200]}...")
    else:
        print(f"Error: {response.get('error', 'unknown error')}")

def test_langgraph_docs_resource(process):
    """Test the LangGraph documentation resource."""
    print("\n=== Testing LangGraph Documentation Resource ===")
    
    response = send_request(
        process,
        request_type="resource",
        server_name="LangGraph-Docs-MCP-Server",
        uri="docs://langgraph/full"
    )
    
    print(f"Response status: {response.get('status', 'unknown')}")
    if response.get("status") == "success":
        # Print just the first 200 characters of the result for brevity
        result = response.get("result", "")
        print(f"Result preview: {result[:200]}...")
    else:
        print(f"Error: {response.get('error', 'unknown error')}")

def test_weather_tool(process):
    """Test the weather tool."""
    print("\n=== Testing Weather Tool ===")
    
    response = send_request(
        process,
        request_type="tool",
        server_name="LangGraph-Docs-MCP-Server",
        tool_name="get_weather",
        arguments={"city": "San Francisco"}
    )
    
    print(f"Response status: {response.get('status', 'unknown')}")
    if response.get("status") == "success":
        result = response.get("result", "")
        print(f"Result: {result}")
    else:
        print(f"Error: {response.get('error', 'unknown error')}")

def test_weather_resource(process):
    """Test the weather resource."""
    print("\n=== Testing Weather Resource ===")
    
    response = send_request(
        process,
        request_type="resource",
        server_name="LangGraph-Docs-MCP-Server",
        uri="weather://locations/popular"
    )
    
    print(f"Response status: {response.get('status', 'unknown')}")
    if response.get("status") == "success":
        result = response.get("result", "")
        print(f"Result: {result}")
    else:
        print(f"Error: {response.get('error', 'unknown error')}")

def main():
    """Run the test script."""
    # Start the MCP server
    process = start_mcp_server()
    
    try:
        # Test the LangGraph tools and resources
        test_langgraph_query_tool(process)
        test_langgraph_docs_resource(process)
        
        # Test the Weather tools and resources
        # Note: These will fail unless you uncomment the weather modules in the __init__.py files
        # test_weather_tool(process)
        # test_weather_resource(process)
        
    finally:
        # Clean up
        print("\nShutting down MCP server...")
        process.terminate()
        process.wait()

if __name__ == "__main__":
    main()