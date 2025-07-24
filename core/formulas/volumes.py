"""
Volume calculations for 3D geometric shapes.
Contains formulas for calculating volumes of various three-dimensional objects.
"""

import math


def volume_cube(side):
    """Calculate the volume of a cube."""
    if side < 0:
        raise ValueError("Side length cannot be negative")
    return side ** 3


def volume_rectangular_prism(length, width, height):
    """Calculate the volume of a rectangular prism (box)."""
    if length < 0 or width < 0 or height < 0:
        raise ValueError("Dimensions cannot be negative")
    return length * width * height


def volume_sphere(radius):
    """Calculate the volume of a sphere."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return (4/3) * math.pi * radius ** 3


def volume_cylinder(radius, height):
    """Calculate the volume of a cylinder."""
    if radius < 0 or height < 0:
        raise ValueError("Dimensions cannot be negative")
    return math.pi * radius ** 2 * height


def volume_cone(radius, height):
    """Calculate the volume of a cone."""
    if radius < 0 or height < 0:
        raise ValueError("Dimensions cannot be negative")
    return (1/3) * math.pi * radius ** 2 * height


def volume_pyramid(base_area, height):
    """Calculate the volume of a pyramid."""
    if base_area < 0 or height < 0:
        raise ValueError("Dimensions cannot be negative")
    return (1/3) * base_area * height


def volume_ellipsoid(a, b, c):
    """Calculate the volume of an ellipsoid."""
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Semi-axes cannot be negative")
    return (4/3) * math.pi * a * b * c


def surface_area_sphere(radius):
    """Calculate the surface area of a sphere."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 4 * math.pi * radius ** 2


def surface_area_cylinder(radius, height):
    """Calculate the surface area of a cylinder."""
    if radius < 0 or height < 0:
        raise ValueError("Dimensions cannot be negative")
    return 2 * math.pi * radius * (radius + height)


def surface_area_cone(radius, slant_height):
    """Calculate the surface area of a cone."""
    if radius < 0 or slant_height < 0:
        raise ValueError("Dimensions cannot be negative")
    return math.pi * radius * (radius + slant_height)
