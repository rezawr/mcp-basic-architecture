"""
Logging utilities for the MCP server.
This module provides logging functionality for the application.
"""
import logging
import sys
from datetime import datetime

def setup_logger(name, level=logging.INFO):
    """
    Set up a logger with the specified name and level.
    
    Args:
        name (str): The name of the logger
        level (int): The logging level (default: logging.INFO)
        
    Returns:
        logging.Logger: The configured logger
    """
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Create console handler and set level
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Add formatter to handler
    handler.setFormatter(formatter)
    
    # Add handler to logger
    logger.addHandler(handler)
    
    return logger

def log_tool_call(logger, tool_name, args):
    """
    Log a tool call with its arguments.
    
    Args:
        logger (logging.Logger): The logger to use
        tool_name (str): The name of the tool being called
        args (dict): The arguments passed to the tool
    """
    logger.info(f"Tool call: {tool_name} with args: {args}")

def log_resource_access(logger, resource_uri):
    """
    Log a resource access.
    
    Args:
        logger (logging.Logger): The logger to use
        resource_uri (str): The URI of the resource being accessed
    """
    logger.info(f"Resource access: {resource_uri}")