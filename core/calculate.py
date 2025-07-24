"""
Core calculation dispatch function for the Math Calculation Engine.
Provides strict argument validation and operation routing.
"""

from .operations import OPERATION_MAP


def calculate(*, operation, **kwargs):
    """
    Central calculation function that dispatches to specific operations.
    
    Args:
        operation: Operation enum value specifying which calculation to perform
        **kwargs: Named arguments required for the specific operation
        
    Returns:
        The result of the calculation
        
    Raises:
        ValueError: If operation is unsupported, arguments are missing, or unexpected arguments provided
        
    Example:
        >>> from core.operations import Operation
        >>> calculate(operation=Operation.ADD, a=5, b=3)
        8
        >>> calculate(operation=Operation.AREA_CIRCLE, radius=10)
        314.1592653589793
    """
    # Check if operation is supported
    config = OPERATION_MAP.get(operation)
    if not config:
        raise ValueError(f"Unsupported operation: {operation}")

    # Get required arguments for this operation
    required = config["required"]
    
    # Check for missing required arguments
    missing = [arg for arg in required if arg not in kwargs]
    if missing:
        raise ValueError(f"Missing required arguments: {', '.join(missing)}")

    # Check for unexpected arguments
    unexpected = [arg for arg in kwargs if arg not in required]
    if unexpected:
        raise ValueError(f"Unexpected arguments: {', '.join(unexpected)}")

    # All validation passed, execute the operation
    try:
        return config["func"](**kwargs)
    except Exception as e:
        raise ValueError(f"Calculation error: {str(e)}")


def get_operation_info(operation):
    """
    Get information about a specific operation.
    
    Args:
        operation: Operation enum value
        
    Returns:
        Dictionary with operation details including required arguments
    """
    config = OPERATION_MAP.get(operation)
    if not config:
        return None
    
    return {
        "operation": operation,
        "required_args": config["required"],
        "function_name": config["func"].__name__,
        "docstring": config["func"].__doc__
    }


def list_operations():
    """
    List all available operations and their required arguments.
    
    Returns:
        List of dictionaries containing operation information
    """
    return [get_operation_info(op) for op in OPERATION_MAP.keys()]
