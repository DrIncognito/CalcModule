"""
Geometry operations for the Math Calculation Engine.
Contains formulas for calculating areas, perimeters, and volumes of geometric shapes.
"""

import math


# Area calculations
def area_circle(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2


def area_rectangle(length, width):
    """Calculate the area of a rectangle."""
    if length < 0 or width < 0:
        raise ValueError("Dimensions cannot be negative")
    return length * width


def area_square(side):
    """Calculate the area of a square."""
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return side ** 2


def area_triangle(base, height):
    """Calculate the area of a triangle using base and height."""
    if base < 0 or height < 0:
        raise ValueError("Dimensions cannot be negative")
    return 0.5 * base * height


def area_triangle_heron(a, b, c):
    """Calculate the area of a triangle using Heron's formula."""
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle - triangle inequality violated")
    
    s = (a + b + c) / 2  # semi-perimeter
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def area_rhombus(diagonal1, diagonal2):
    """Calculate the area of a rhombus using diagonals."""
    if diagonal1 < 0 or diagonal2 < 0:
        raise ValueError("Diagonal lengths cannot be negative")
    return (diagonal1 * diagonal2) / 2


def area_trapezoid(base1, base2, height):
    """Calculate the area of a trapezoid."""
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError("Dimensions cannot be negative")
    return ((base1 + base2) * height) / 2


def area_regular_polygon(perimeter, apothem):
    """Calculate the area of a regular polygon."""
    if perimeter < 0 or apothem < 0:
        raise ValueError("Dimensions cannot be negative")
    return (perimeter * apothem) / 2


def area_ellipse(semi_major_axis, semi_minor_axis):
    """Calculate the area of an ellipse."""
    if semi_major_axis < 0 or semi_minor_axis < 0:
        raise ValueError("Semi-axes cannot be negative")
    return math.pi * semi_major_axis * semi_minor_axis


def area_sector(radius, angle_degrees):
    """Calculate the area of a circular sector."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    if angle_degrees < 0 or angle_degrees > 360:
        raise ValueError("Angle must be between 0 and 360 degrees")
    return (angle_degrees / 360) * math.pi * radius ** 2


def area_annulus(outer_radius, inner_radius):
    """Calculate the area of an annulus (ring)."""
    if outer_radius < 0 or inner_radius < 0:
        raise ValueError("Radii cannot be negative")
    if inner_radius >= outer_radius:
        raise ValueError("Inner radius must be less than outer radius")
    return math.pi * (outer_radius ** 2 - inner_radius ** 2)


# Perimeter/Circumference calculations
def circumference_circle(radius):
    """Calculate the circumference of a circle."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 2 * math.pi * radius


def perimeter_rectangle(length, width):
    """Calculate the perimeter of a rectangle."""
    if length < 0 or width < 0:
        raise ValueError("Dimensions cannot be negative")
    return 2 * (length + width)


def perimeter_square(side):
    """Calculate the perimeter of a square."""
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return 4 * side


def perimeter_triangle(a, b, c):
    """Calculate the perimeter of a triangle."""
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive")
    return a + b + c


def perimeter_regular_polygon(num_sides, side_length):
    """Calculate the perimeter of a regular polygon."""
    if num_sides < 3:
        raise ValueError("A polygon must have at least 3 sides")
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return num_sides * side_length


def perimeter_ellipse_approximation(semi_major_axis, semi_minor_axis):
    """Calculate approximate perimeter of an ellipse using Ramanujan's approximation."""
    if semi_major_axis < 0 or semi_minor_axis < 0:
        raise ValueError("Semi-axes cannot be negative")
    
    a, b = semi_major_axis, semi_minor_axis
    h = ((a - b) ** 2) / ((a + b) ** 2)
    return math.pi * (a + b) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))


# Distance and other geometric calculations
def distance_2d(x1, y1, x2, y2):
    """Calculate distance between two points in 2D space."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def distance_3d(x1, y1, z1, x2, y2, z2):
    """Calculate distance between two points in 3D space."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def midpoint_2d(x1, y1, x2, y2):
    """Calculate midpoint between two points in 2D space."""
    return ((x1 + x2) / 2, (y1 + y2) / 2)


def slope_line(x1, y1, x2, y2):
    """Calculate the slope of a line between two points."""
    if x2 == x1:
        raise ValueError("Slope is undefined for vertical lines")
    return (y2 - y1) / (x2 - x1)


def angle_between_vectors(x1, y1, x2, y2):
    """Calculate angle between two vectors in degrees."""
    dot_product = x1 * x2 + y1 * y2
    magnitude1 = math.sqrt(x1 ** 2 + y1 ** 2)
    magnitude2 = math.sqrt(x2 ** 2 + y2 ** 2)
    
    if magnitude1 == 0 or magnitude2 == 0:
        raise ValueError("Cannot calculate angle with zero vector")
    
    cos_angle = dot_product / (magnitude1 * magnitude2)
    # Clamp to [-1, 1] to handle floating point errors
    cos_angle = max(-1, min(1, cos_angle))
    
    return math.degrees(math.acos(cos_angle))
