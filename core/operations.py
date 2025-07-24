"""
Operations enum and mapping for the Math Calculation Engine.
Defines all supported operations and their required parameters.
"""

from enum import Enum, auto
from .formulas.arithmetic import (
    add, subtract, multiply, divide, modulo, floor_divide, power, square_root, cube_root, nth_root,
    square, cube, absolute_value, sign, ceiling, floor, round_to_decimals, factorial, combination,
    permutation, greatest_common_divisor, least_common_multiple, is_prime, fibonacci,
    arithmetic_mean, geometric_mean, harmonic_mean, percentage, percentage_change
)
from .formulas.geometry import (
    area_circle, area_rectangle, area_square, area_triangle, area_triangle_heron, area_rhombus,
    area_trapezoid, area_regular_polygon, area_ellipse, area_sector, area_annulus,
    circumference_circle, perimeter_rectangle, perimeter_square, perimeter_triangle,
    perimeter_regular_polygon, perimeter_ellipse_approximation, distance_2d, distance_3d,
    midpoint_2d, slope_line, angle_between_vectors
)
from .formulas.volumes import (
    volume_cube, volume_rectangular_prism, volume_sphere, volume_cylinder, volume_cone,
    volume_pyramid, volume_ellipsoid, surface_area_sphere, surface_area_cylinder, surface_area_cone
)
from .formulas.trigonometry import (
    sin_degrees, cos_degrees, tan_degrees, sin_radians, cos_radians, tan_radians,
    asin_degrees, acos_degrees, atan_degrees, asin_radians, acos_radians, atan_radians,
    atan2_degrees, atan2_radians, sec_degrees, csc_degrees, cot_degrees,
    degrees_to_radians, radians_to_degrees
)
from .formulas.logarithms import (
    natural_log, log_base_10, log_base_2, log_custom_base, exponential_e, exponential_base_10,
    exponential_base_2, exponential_custom_base, sinh, cosh, tanh, asinh, acosh, atanh
)
from .formulas.statistics import (
    mean, median, mode, variance_population, variance_sample, standard_deviation_population,
    standard_deviation_sample, range_values, quartile_1, quartile_3, interquartile_range,
    correlation_coefficient, z_score, percentile
)


class Operation(Enum):
    """Enumeration of all supported mathematical operations."""
    # Basic Arithmetic
    ADD = auto()
    SUBTRACT = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    MODULO = auto()
    FLOOR_DIVIDE = auto()
    
    # Power and Root Operations
    POWER = auto()
    SQUARE_ROOT = auto()
    CUBE_ROOT = auto()
    NTH_ROOT = auto()
    SQUARE = auto()
    CUBE = auto()
    
    # Advanced Arithmetic
    ABSOLUTE_VALUE = auto()
    SIGN = auto()
    CEILING = auto()
    FLOOR = auto()
    ROUND_TO_DECIMALS = auto()
    FACTORIAL = auto()
    COMBINATION = auto()
    PERMUTATION = auto()
    GCD = auto()
    LCM = auto()
    IS_PRIME = auto()
    FIBONACCI = auto()
    ARITHMETIC_MEAN = auto()
    GEOMETRIC_MEAN = auto()
    HARMONIC_MEAN = auto()
    PERCENTAGE = auto()
    PERCENTAGE_CHANGE = auto()
    
    # Area Calculations
    AREA_CIRCLE = auto()
    AREA_RECTANGLE = auto()
    AREA_SQUARE = auto()
    AREA_TRIANGLE = auto()
    AREA_TRIANGLE_HERON = auto()
    AREA_RHOMBUS = auto()
    AREA_TRAPEZOID = auto()
    AREA_REGULAR_POLYGON = auto()
    AREA_ELLIPSE = auto()
    AREA_SECTOR = auto()
    AREA_ANNULUS = auto()
    
    # Perimeter/Circumference
    CIRCUMFERENCE_CIRCLE = auto()
    PERIMETER_RECTANGLE = auto()
    PERIMETER_SQUARE = auto()
    PERIMETER_TRIANGLE = auto()
    PERIMETER_REGULAR_POLYGON = auto()
    PERIMETER_ELLIPSE = auto()
    
    # Distance and Geometry
    DISTANCE_2D = auto()
    DISTANCE_3D = auto()
    MIDPOINT_2D = auto()
    SLOPE_LINE = auto()
    ANGLE_BETWEEN_VECTORS = auto()
    
    # Volume and Surface Area
    VOLUME_CUBE = auto()
    VOLUME_RECTANGULAR_PRISM = auto()
    VOLUME_SPHERE = auto()
    VOLUME_CYLINDER = auto()
    VOLUME_CONE = auto()
    VOLUME_PYRAMID = auto()
    VOLUME_ELLIPSOID = auto()
    SURFACE_AREA_SPHERE = auto()
    SURFACE_AREA_CYLINDER = auto()
    SURFACE_AREA_CONE = auto()
    
    # Trigonometry
    SIN_DEGREES = auto()
    COS_DEGREES = auto()
    TAN_DEGREES = auto()
    SIN_RADIANS = auto()
    COS_RADIANS = auto()
    TAN_RADIANS = auto()
    ASIN_DEGREES = auto()
    ACOS_DEGREES = auto()
    ATAN_DEGREES = auto()
    ASIN_RADIANS = auto()
    ACOS_RADIANS = auto()
    ATAN_RADIANS = auto()
    ATAN2_DEGREES = auto()
    ATAN2_RADIANS = auto()
    SEC_DEGREES = auto()
    CSC_DEGREES = auto()
    COT_DEGREES = auto()
    DEGREES_TO_RADIANS = auto()
    RADIANS_TO_DEGREES = auto()
    
    # Logarithms and Exponentials
    NATURAL_LOG = auto()
    LOG_BASE_10 = auto()
    LOG_BASE_2 = auto()
    LOG_CUSTOM_BASE = auto()
    EXPONENTIAL_E = auto()
    EXPONENTIAL_BASE_10 = auto()
    EXPONENTIAL_BASE_2 = auto()
    EXPONENTIAL_CUSTOM_BASE = auto()
    SINH = auto()
    COSH = auto()
    TANH = auto()
    ASINH = auto()
    ACOSH = auto()
    ATANH = auto()
    
    # Statistics
    MEAN = auto()
    MEDIAN = auto()
    MODE = auto()
    VARIANCE_POPULATION = auto()
    VARIANCE_SAMPLE = auto()
    STANDARD_DEVIATION_POPULATION = auto()
    STANDARD_DEVIATION_SAMPLE = auto()
    RANGE_VALUES = auto()
    QUARTILE_1 = auto()
    QUARTILE_3 = auto()
    INTERQUARTILE_RANGE = auto()
    CORRELATION_COEFFICIENT = auto()
    Z_SCORE = auto()
    PERCENTILE = auto()


# Operation mapping with function references and required parameters
OPERATION_MAP = {
    # Basic Arithmetic
    Operation.ADD: {
        "func": add,
        "required": ["a", "b"]
    },
    Operation.SUBTRACT: {
        "func": subtract,
        "required": ["a", "b"]
    },
    Operation.MULTIPLY: {
        "func": multiply,
        "required": ["a", "b"]
    },
    Operation.DIVIDE: {
        "func": divide,
        "required": ["a", "b"]
    },
    Operation.MODULO: {
        "func": modulo,
        "required": ["a", "b"]
    },
    Operation.FLOOR_DIVIDE: {
        "func": floor_divide,
        "required": ["a", "b"]
    },
    
    # Power and Root Operations
    Operation.POWER: {
        "func": power,
        "required": ["num", "power"]
    },
    Operation.SQUARE_ROOT: {
        "func": square_root,
        "required": ["num"]
    },
    Operation.CUBE_ROOT: {
        "func": cube_root,
        "required": ["num"]
    },
    Operation.NTH_ROOT: {
        "func": nth_root,
        "required": ["num", "n"]
    },
    Operation.SQUARE: {
        "func": square,
        "required": ["num"]
    },
    Operation.CUBE: {
        "func": cube,
        "required": ["num"]
    },
    
    # Advanced Arithmetic
    Operation.ABSOLUTE_VALUE: {
        "func": absolute_value,
        "required": ["num"]
    },
    Operation.SIGN: {
        "func": sign,
        "required": ["num"]
    },
    Operation.CEILING: {
        "func": ceiling,
        "required": ["num"]
    },
    Operation.FLOOR: {
        "func": floor,
        "required": ["num"]
    },
    Operation.ROUND_TO_DECIMALS: {
        "func": round_to_decimals,
        "required": ["num", "decimals"]
    },
    Operation.FACTORIAL: {
        "func": factorial,
        "required": ["n"]
    },
    Operation.COMBINATION: {
        "func": combination,
        "required": ["n", "r"]
    },
    Operation.PERMUTATION: {
        "func": permutation,
        "required": ["n", "r"]
    },
    Operation.GCD: {
        "func": greatest_common_divisor,
        "required": ["a", "b"]
    },
    Operation.LCM: {
        "func": least_common_multiple,
        "required": ["a", "b"]
    },
    Operation.IS_PRIME: {
        "func": is_prime,
        "required": ["n"]
    },
    Operation.FIBONACCI: {
        "func": fibonacci,
        "required": ["n"]
    },
    Operation.ARITHMETIC_MEAN: {
        "func": arithmetic_mean,
        "required": ["a", "b"]
    },
    Operation.GEOMETRIC_MEAN: {
        "func": geometric_mean,
        "required": ["a", "b"]
    },
    Operation.HARMONIC_MEAN: {
        "func": harmonic_mean,
        "required": ["a", "b"]
    },
    Operation.PERCENTAGE: {
        "func": percentage,
        "required": ["part", "whole"]
    },
    Operation.PERCENTAGE_CHANGE: {
        "func": percentage_change,
        "required": ["old_value", "new_value"]
    },
    
    # Area Calculations
    Operation.AREA_CIRCLE: {
        "func": area_circle,
        "required": ["radius"]
    },
    Operation.AREA_RECTANGLE: {
        "func": area_rectangle,
        "required": ["length", "width"]
    },
    Operation.AREA_SQUARE: {
        "func": area_square,
        "required": ["side"]
    },
    Operation.AREA_TRIANGLE: {
        "func": area_triangle,
        "required": ["base", "height"]
    },
    Operation.AREA_TRIANGLE_HERON: {
        "func": area_triangle_heron,
        "required": ["a", "b", "c"]
    },
    Operation.AREA_RHOMBUS: {
        "func": area_rhombus,
        "required": ["diagonal1", "diagonal2"]
    },
    Operation.AREA_TRAPEZOID: {
        "func": area_trapezoid,
        "required": ["base1", "base2", "height"]
    },
    Operation.AREA_REGULAR_POLYGON: {
        "func": area_regular_polygon,
        "required": ["perimeter", "apothem"]
    },
    Operation.AREA_ELLIPSE: {
        "func": area_ellipse,
        "required": ["semi_major_axis", "semi_minor_axis"]
    },
    Operation.AREA_SECTOR: {
        "func": area_sector,
        "required": ["radius", "angle_degrees"]
    },
    Operation.AREA_ANNULUS: {
        "func": area_annulus,
        "required": ["outer_radius", "inner_radius"]
    },
    
    # Perimeter/Circumference
    Operation.CIRCUMFERENCE_CIRCLE: {
        "func": circumference_circle,
        "required": ["radius"]
    },
    Operation.PERIMETER_RECTANGLE: {
        "func": perimeter_rectangle,
        "required": ["length", "width"]
    },
    Operation.PERIMETER_SQUARE: {
        "func": perimeter_square,
        "required": ["side"]
    },
    Operation.PERIMETER_TRIANGLE: {
        "func": perimeter_triangle,
        "required": ["a", "b", "c"]
    },
    Operation.PERIMETER_REGULAR_POLYGON: {
        "func": perimeter_regular_polygon,
        "required": ["num_sides", "side_length"]
    },
    Operation.PERIMETER_ELLIPSE: {
        "func": perimeter_ellipse_approximation,
        "required": ["semi_major_axis", "semi_minor_axis"]
    },
    
    # Distance and Geometry
    Operation.DISTANCE_2D: {
        "func": distance_2d,
        "required": ["x1", "y1", "x2", "y2"]
    },
    Operation.DISTANCE_3D: {
        "func": distance_3d,
        "required": ["x1", "y1", "z1", "x2", "y2", "z2"]
    },
    Operation.MIDPOINT_2D: {
        "func": midpoint_2d,
        "required": ["x1", "y1", "x2", "y2"]
    },
    Operation.SLOPE_LINE: {
        "func": slope_line,
        "required": ["x1", "y1", "x2", "y2"]
    },
    Operation.ANGLE_BETWEEN_VECTORS: {
        "func": angle_between_vectors,
        "required": ["x1", "y1", "x2", "y2"]
    },
    
    # Volume and Surface Area
    Operation.VOLUME_CUBE: {
        "func": volume_cube,
        "required": ["side"]
    },
    Operation.VOLUME_RECTANGULAR_PRISM: {
        "func": volume_rectangular_prism,
        "required": ["length", "width", "height"]
    },
    Operation.VOLUME_SPHERE: {
        "func": volume_sphere,
        "required": ["radius"]
    },
    Operation.VOLUME_CYLINDER: {
        "func": volume_cylinder,
        "required": ["radius", "height"]
    },
    Operation.VOLUME_CONE: {
        "func": volume_cone,
        "required": ["radius", "height"]
    },
    Operation.VOLUME_PYRAMID: {
        "func": volume_pyramid,
        "required": ["base_area", "height"]
    },
    Operation.VOLUME_ELLIPSOID: {
        "func": volume_ellipsoid,
        "required": ["a", "b", "c"]
    },
    Operation.SURFACE_AREA_SPHERE: {
        "func": surface_area_sphere,
        "required": ["radius"]
    },
    Operation.SURFACE_AREA_CYLINDER: {
        "func": surface_area_cylinder,
        "required": ["radius", "height"]
    },
    Operation.SURFACE_AREA_CONE: {
        "func": surface_area_cone,
        "required": ["radius", "slant_height"]
    },
    
    # Trigonometry
    Operation.SIN_DEGREES: {
        "func": sin_degrees,
        "required": ["angle_degrees"]
    },
    Operation.COS_DEGREES: {
        "func": cos_degrees,
        "required": ["angle_degrees"]
    },
    Operation.TAN_DEGREES: {
        "func": tan_degrees,
        "required": ["angle_degrees"]
    },
    Operation.SIN_RADIANS: {
        "func": sin_radians,
        "required": ["angle_radians"]
    },
    Operation.COS_RADIANS: {
        "func": cos_radians,
        "required": ["angle_radians"]
    },
    Operation.TAN_RADIANS: {
        "func": tan_radians,
        "required": ["angle_radians"]
    },
    Operation.ASIN_DEGREES: {
        "func": asin_degrees,
        "required": ["value"]
    },
    Operation.ACOS_DEGREES: {
        "func": acos_degrees,
        "required": ["value"]
    },
    Operation.ATAN_DEGREES: {
        "func": atan_degrees,
        "required": ["value"]
    },
    Operation.ASIN_RADIANS: {
        "func": asin_radians,
        "required": ["value"]
    },
    Operation.ACOS_RADIANS: {
        "func": acos_radians,
        "required": ["value"]
    },
    Operation.ATAN_RADIANS: {
        "func": atan_radians,
        "required": ["value"]
    },
    Operation.ATAN2_DEGREES: {
        "func": atan2_degrees,
        "required": ["y", "x"]
    },
    Operation.ATAN2_RADIANS: {
        "func": atan2_radians,
        "required": ["y", "x"]
    },
    Operation.SEC_DEGREES: {
        "func": sec_degrees,
        "required": ["angle_degrees"]
    },
    Operation.CSC_DEGREES: {
        "func": csc_degrees,
        "required": ["angle_degrees"]
    },
    Operation.COT_DEGREES: {
        "func": cot_degrees,
        "required": ["angle_degrees"]
    },
    Operation.DEGREES_TO_RADIANS: {
        "func": degrees_to_radians,
        "required": ["degrees"]
    },
    Operation.RADIANS_TO_DEGREES: {
        "func": radians_to_degrees,
        "required": ["radians"]
    },
    
    # Logarithms and Exponentials
    Operation.NATURAL_LOG: {
        "func": natural_log,
        "required": ["x"]
    },
    Operation.LOG_BASE_10: {
        "func": log_base_10,
        "required": ["x"]
    },
    Operation.LOG_BASE_2: {
        "func": log_base_2,
        "required": ["x"]
    },
    Operation.LOG_CUSTOM_BASE: {
        "func": log_custom_base,
        "required": ["x", "base"]
    },
    Operation.EXPONENTIAL_E: {
        "func": exponential_e,
        "required": ["x"]
    },
    Operation.EXPONENTIAL_BASE_10: {
        "func": exponential_base_10,
        "required": ["x"]
    },
    Operation.EXPONENTIAL_BASE_2: {
        "func": exponential_base_2,
        "required": ["x"]
    },
    Operation.EXPONENTIAL_CUSTOM_BASE: {
        "func": exponential_custom_base,
        "required": ["base", "exponent"]
    },
    Operation.SINH: {
        "func": sinh,
        "required": ["x"]
    },
    Operation.COSH: {
        "func": cosh,
        "required": ["x"]
    },
    Operation.TANH: {
        "func": tanh,
        "required": ["x"]
    },
    Operation.ASINH: {
        "func": asinh,
        "required": ["x"]
    },
    Operation.ACOSH: {
        "func": acosh,
        "required": ["x"]
    },
    Operation.ATANH: {
        "func": atanh,
        "required": ["x"]
    },
    
    # Statistics
    Operation.MEAN: {
        "func": mean,
        "required": ["values"]
    },
    Operation.MEDIAN: {
        "func": median,
        "required": ["values"]
    },
    Operation.MODE: {
        "func": mode,
        "required": ["values"]
    },
    Operation.VARIANCE_POPULATION: {
        "func": variance_population,
        "required": ["values"]
    },
    Operation.VARIANCE_SAMPLE: {
        "func": variance_sample,
        "required": ["values"]
    },
    Operation.STANDARD_DEVIATION_POPULATION: {
        "func": standard_deviation_population,
        "required": ["values"]
    },
    Operation.STANDARD_DEVIATION_SAMPLE: {
        "func": standard_deviation_sample,
        "required": ["values"]
    },
    Operation.RANGE_VALUES: {
        "func": range_values,
        "required": ["values"]
    },
    Operation.QUARTILE_1: {
        "func": quartile_1,
        "required": ["values"]
    },
    Operation.QUARTILE_3: {
        "func": quartile_3,
        "required": ["values"]
    },
    Operation.INTERQUARTILE_RANGE: {
        "func": interquartile_range,
        "required": ["values"]
    },
    Operation.CORRELATION_COEFFICIENT: {
        "func": correlation_coefficient,
        "required": ["x_values", "y_values"]
    },
    Operation.Z_SCORE: {
        "func": z_score,
        "required": ["value", "population_mean", "population_std"]
    },
    Operation.PERCENTILE: {
        "func": percentile,
        "required": ["values", "percentile_rank"]
    }
}
