"""
Trigonometric functions and calculations.
Contains basic and advanced trigonometric operations.
"""

import math


def sin_degrees(angle_degrees):
    """Calculate sine of angle in degrees."""
    return math.sin(math.radians(angle_degrees))


def cos_degrees(angle_degrees):
    """Calculate cosine of angle in degrees."""
    return math.cos(math.radians(angle_degrees))


def tan_degrees(angle_degrees):
    """Calculate tangent of angle in degrees."""
    return math.tan(math.radians(angle_degrees))


def sin_radians(angle_radians):
    """Calculate sine of angle in radians."""
    return math.sin(angle_radians)


def cos_radians(angle_radians):
    """Calculate cosine of angle in radians."""
    return math.cos(angle_radians)


def tan_radians(angle_radians):
    """Calculate tangent of angle in radians."""
    return math.tan(angle_radians)


def asin_degrees(value):
    """Calculate arcsine in degrees."""
    if value < -1 or value > 1:
        raise ValueError("Value must be between -1 and 1")
    return math.degrees(math.asin(value))


def acos_degrees(value):
    """Calculate arccosine in degrees."""
    if value < -1 or value > 1:
        raise ValueError("Value must be between -1 and 1")
    return math.degrees(math.acos(value))


def atan_degrees(value):
    """Calculate arctangent in degrees."""
    return math.degrees(math.atan(value))


def asin_radians(value):
    """Calculate arcsine in radians."""
    if value < -1 or value > 1:
        raise ValueError("Value must be between -1 and 1")
    return math.asin(value)


def acos_radians(value):
    """Calculate arccosine in radians."""
    if value < -1 or value > 1:
        raise ValueError("Value must be between -1 and 1")
    return math.acos(value)


def atan_radians(value):
    """Calculate arctangent in radians."""
    return math.atan(value)


def atan2_degrees(y, x):
    """Calculate two-argument arctangent in degrees."""
    return math.degrees(math.atan2(y, x))


def atan2_radians(y, x):
    """Calculate two-argument arctangent in radians."""
    return math.atan2(y, x)


def sec_degrees(angle_degrees):
    """Calculate secant of angle in degrees."""
    cos_val = math.cos(math.radians(angle_degrees))
    if abs(cos_val) < 1e-10:
        raise ValueError("Secant undefined (cosine is zero)")
    return 1 / cos_val


def csc_degrees(angle_degrees):
    """Calculate cosecant of angle in degrees."""
    sin_val = math.sin(math.radians(angle_degrees))
    if abs(sin_val) < 1e-10:
        raise ValueError("Cosecant undefined (sine is zero)")
    return 1 / sin_val


def cot_degrees(angle_degrees):
    """Calculate cotangent of angle in degrees."""
    tan_val = math.tan(math.radians(angle_degrees))
    if abs(tan_val) < 1e-10:
        raise ValueError("Cotangent undefined (tangent is zero)")
    return 1 / tan_val


def degrees_to_radians(degrees):
    """Convert degrees to radians."""
    return math.radians(degrees)


def radians_to_degrees(radians):
    """Convert radians to degrees."""
    return math.degrees(radians)
