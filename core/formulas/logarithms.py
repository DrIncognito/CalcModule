"""
Logarithmic and exponential functions.
Contains natural logarithms, common logarithms, and exponential calculations.
"""

import math


def natural_log(x):
    """Calculate natural logarithm (base e)."""
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers")
    return math.log(x)


def log_base_10(x):
    """Calculate logarithm base 10."""
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers")
    return math.log10(x)


def log_base_2(x):
    """Calculate logarithm base 2."""
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers")
    return math.log2(x)


def log_custom_base(x, base):
    """Calculate logarithm with custom base."""
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers")
    if base <= 0 or base == 1:
        raise ValueError("Base must be positive and not equal to 1")
    return math.log(x) / math.log(base)


def exponential_e(x):
    """Calculate e raised to the power x."""
    return math.exp(x)


def exponential_base_10(x):
    """Calculate 10 raised to the power x."""
    return 10 ** x


def exponential_base_2(x):
    """Calculate 2 raised to the power x."""
    return 2 ** x


def exponential_custom_base(base, exponent):
    """Calculate base raised to the given exponent."""
    if base == 0 and exponent <= 0:
        raise ValueError("0 raised to non-positive power is undefined")
    return base ** exponent


def sinh(x):
    """Calculate hyperbolic sine."""
    return math.sinh(x)


def cosh(x):
    """Calculate hyperbolic cosine."""
    return math.cosh(x)


def tanh(x):
    """Calculate hyperbolic tangent."""
    return math.tanh(x)


def asinh(x):
    """Calculate inverse hyperbolic sine."""
    return math.asinh(x)


def acosh(x):
    """Calculate inverse hyperbolic cosine."""
    if x < 1:
        raise ValueError("Inverse hyperbolic cosine undefined for x < 1")
    return math.acosh(x)


def atanh(x):
    """Calculate inverse hyperbolic tangent."""
    if abs(x) >= 1:
        raise ValueError("Inverse hyperbolic tangent undefined for |x| >= 1")
    return math.atanh(x)
