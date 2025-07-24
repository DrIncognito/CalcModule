"""
Arithmetic operations for the Math Calculation Engine.
Contains basic and advanced mathematical operations.
"""

import math


# Basic arithmetic operations
def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


def modulo(a, b):
    """Calculate a modulo b (remainder of a/b)."""
    if b == 0:
        raise ValueError("Modulo by zero is not allowed")
    return a % b


def floor_divide(a, b):
    """Floor division (integer division)."""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a // b


# Power and root operations
def power(num, power):
    """Raise num to the given power."""
    return num ** power


def square_root(num):
    """Calculate the square root of a number."""
    if num < 0:
        raise ValueError("Square root of negative number is not supported")
    return math.sqrt(num)


def cube_root(num):
    """Calculate the cube root of a number."""
    if num >= 0:
        return num ** (1/3)
    else:
        return -((-num) ** (1/3))


def nth_root(num, n):
    """Calculate the nth root of a number."""
    if n == 0:
        raise ValueError("Cannot calculate 0th root")
    if num < 0 and n % 2 == 0:
        raise ValueError("Even root of negative number is not supported")
    
    if num >= 0:
        return num ** (1/n)
    else:
        return -((-num) ** (1/n))


def square(num):
    """Calculate the square of a number."""
    return num ** 2


def cube(num):
    """Calculate the cube of a number."""
    return num ** 3


# Advanced arithmetic operations
def absolute_value(num):
    """Calculate the absolute value of a number."""
    return abs(num)


def sign(num):
    """Return the sign of a number (-1, 0, or 1)."""
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0


def ceiling(num):
    """Round up to the nearest integer."""
    return math.ceil(num)


def floor(num):
    """Round down to the nearest integer."""
    return math.floor(num)


def round_to_decimals(num, decimals):
    """Round to specified number of decimal places."""
    if decimals < 0:
        raise ValueError("Number of decimal places cannot be negative")
    return round(num, decimals)


def factorial(n):
    """Calculate factorial of n."""
    if not isinstance(n, int):
        raise ValueError("Factorial is only defined for integers")
    if n < 0:
        raise ValueError("Factorial of negative number is undefined")
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def combination(n, r):
    """Calculate combination C(n,r) = n! / (r! * (n-r)!)."""
    if not isinstance(n, int) or not isinstance(r, int):
        raise ValueError("Combination is only defined for integers")
    if n < 0 or r < 0:
        raise ValueError("n and r must be non-negative")
    if r > n:
        raise ValueError("r cannot be greater than n")
    
    if r == 0 or r == n:
        return 1
    
    # Use the more efficient formula to avoid large factorials
    r = min(r, n - r)  # Take advantage of symmetry
    result = 1
    for i in range(r):
        result = result * (n - i) // (i + 1)
    return result


def permutation(n, r):
    """Calculate permutation P(n,r) = n! / (n-r)!."""
    if not isinstance(n, int) or not isinstance(r, int):
        raise ValueError("Permutation is only defined for integers")
    if n < 0 or r < 0:
        raise ValueError("n and r must be non-negative")
    if r > n:
        raise ValueError("r cannot be greater than n")
    
    result = 1
    for i in range(n, n - r, -1):
        result *= i
    return result


def greatest_common_divisor(a, b):
    """Calculate the greatest common divisor using Euclidean algorithm."""
    a, b = abs(int(a)), abs(int(b))
    while b:
        a, b = b, a % b
    return a


def least_common_multiple(a, b):
    """Calculate the least common multiple."""
    a, b = abs(int(a)), abs(int(b))
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // greatest_common_divisor(a, b)


def is_prime(n):
    """Check if a number is prime."""
    if not isinstance(n, int):
        raise ValueError("Prime check is only defined for integers")
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if not isinstance(n, int):
        raise ValueError("Fibonacci is only defined for integers")
    if n < 0:
        raise ValueError("Fibonacci index must be non-negative")
    
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def arithmetic_mean(a, b):
    """Calculate arithmetic mean of two numbers."""
    return (a + b) / 2


def geometric_mean(a, b):
    """Calculate geometric mean of two numbers."""
    if a < 0 or b < 0:
        raise ValueError("Geometric mean requires non-negative numbers")
    return math.sqrt(a * b)


def harmonic_mean(a, b):
    """Calculate harmonic mean of two numbers."""
    if a == 0 or b == 0:
        raise ValueError("Harmonic mean undefined when either number is zero")
    return 2 / (1/a + 1/b)


def percentage(part, whole):
    """Calculate what percentage 'part' is of 'whole'."""
    if whole == 0:
        raise ValueError("Cannot calculate percentage of zero")
    return (part / whole) * 100


def percentage_change(old_value, new_value):
    """Calculate percentage change from old value to new value."""
    if old_value == 0:
        raise ValueError("Cannot calculate percentage change from zero")
    return ((new_value - old_value) / old_value) * 100
