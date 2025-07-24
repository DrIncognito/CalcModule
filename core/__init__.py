"""
Core module for the Math Calculation Engine.
Provides the main calculate function and operation definitions.
"""

from .calculate import calculate, get_operation_info, list_operations
from .operations import Operation, OPERATION_MAP

__all__ = ['calculate', 'Operation', 'get_operation_info', 'list_operations', 'OPERATION_MAP']
