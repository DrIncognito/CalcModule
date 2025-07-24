"""
Statistical calculations and functions.
Contains measures of central tendency, dispersion, and probability distributions.
"""

import math
from typing import List


def mean(values: List[float]):
    """Calculate arithmetic mean (average)."""
    if not values:
        raise ValueError("Cannot calculate mean of empty list")
    return sum(values) / len(values)


def median(values: List[float]):
    """Calculate median (middle value)."""
    if not values:
        raise ValueError("Cannot calculate median of empty list")
    
    sorted_values = sorted(values)
    n = len(sorted_values)
    
    if n % 2 == 0:
        # Even number of values - average of two middle values
        return (sorted_values[n//2 - 1] + sorted_values[n//2]) / 2
    else:
        # Odd number of values - middle value
        return sorted_values[n//2]


def mode(values: List[float]):
    """Calculate mode (most frequent value)."""
    if not values:
        raise ValueError("Cannot calculate mode of empty list")
    
    frequency = {}
    for value in values:
        frequency[value] = frequency.get(value, 0) + 1
    
    max_frequency = max(frequency.values())
    modes = [value for value, freq in frequency.items() if freq == max_frequency]
    
    if len(modes) == len(set(values)):
        raise ValueError("No mode found - all values appear equally")
    
    return modes[0] if len(modes) == 1 else modes


def variance_population(values: List[float]):
    """Calculate population variance."""
    if not values:
        raise ValueError("Cannot calculate variance of empty list")
    
    mean_val = mean(values)
    return sum((x - mean_val) ** 2 for x in values) / len(values)


def variance_sample(values: List[float]):
    """Calculate sample variance."""
    if len(values) < 2:
        raise ValueError("Sample variance requires at least 2 values")
    
    mean_val = mean(values)
    return sum((x - mean_val) ** 2 for x in values) / (len(values) - 1)


def standard_deviation_population(values: List[float]):
    """Calculate population standard deviation."""
    return math.sqrt(variance_population(values))


def standard_deviation_sample(values: List[float]):
    """Calculate sample standard deviation."""
    return math.sqrt(variance_sample(values))


def range_values(values: List[float]):
    """Calculate range (max - min)."""
    if not values:
        raise ValueError("Cannot calculate range of empty list")
    return max(values) - min(values)


def quartile_1(values: List[float]):
    """Calculate first quartile (Q1)."""
    if not values:
        raise ValueError("Cannot calculate quartile of empty list")
    
    sorted_values = sorted(values)
    n = len(sorted_values)
    
    if n == 1:
        return sorted_values[0]
    
    # Position of Q1
    pos = (n + 1) / 4
    
    if pos == int(pos):
        return sorted_values[int(pos) - 1]
    else:
        lower = int(pos) - 1
        upper = int(pos)
        fraction = pos - int(pos)
        return sorted_values[lower] + fraction * (sorted_values[upper] - sorted_values[lower])


def quartile_3(values: List[float]):
    """Calculate third quartile (Q3)."""
    if not values:
        raise ValueError("Cannot calculate quartile of empty list")
    
    sorted_values = sorted(values)
    n = len(sorted_values)
    
    if n == 1:
        return sorted_values[0]
    
    # Position of Q3
    pos = 3 * (n + 1) / 4
    
    if pos == int(pos):
        return sorted_values[int(pos) - 1]
    else:
        lower = int(pos) - 1
        upper = min(int(pos), n - 1)
        fraction = pos - int(pos)
        return sorted_values[lower] + fraction * (sorted_values[upper] - sorted_values[lower])


def interquartile_range(values: List[float]):
    """Calculate interquartile range (Q3 - Q1)."""
    return quartile_3(values) - quartile_1(values)


def correlation_coefficient(x_values: List[float], y_values: List[float]):
    """Calculate Pearson correlation coefficient."""
    if len(x_values) != len(y_values):
        raise ValueError("x and y lists must have the same length")
    if len(x_values) < 2:
        raise ValueError("Need at least 2 data points for correlation")
    
    n = len(x_values)
    mean_x = mean(x_values)
    mean_y = mean(y_values)
    
    numerator = sum((x_values[i] - mean_x) * (y_values[i] - mean_y) for i in range(n))
    
    sum_sq_x = sum((x - mean_x) ** 2 for x in x_values)
    sum_sq_y = sum((y - mean_y) ** 2 for y in y_values)
    
    denominator = math.sqrt(sum_sq_x * sum_sq_y)
    
    if denominator == 0:
        raise ValueError("Correlation undefined - one variable has no variation")
    
    return numerator / denominator


def z_score(value: float, population_mean: float, population_std: float):
    """Calculate z-score (standard score)."""
    if population_std <= 0:
        raise ValueError("Standard deviation must be positive")
    return (value - population_mean) / population_std


def percentile(values: List[float], percentile_rank: float):
    """Calculate the value at a given percentile."""
    if not values:
        raise ValueError("Cannot calculate percentile of empty list")
    if not 0 <= percentile_rank <= 100:
        raise ValueError("Percentile rank must be between 0 and 100")
    
    sorted_values = sorted(values)
    n = len(sorted_values)
    
    if percentile_rank == 0:
        return sorted_values[0]
    if percentile_rank == 100:
        return sorted_values[-1]
    
    # Calculate position
    pos = percentile_rank / 100 * (n - 1)
    
    if pos == int(pos):
        return sorted_values[int(pos)]
    else:
        lower = int(pos)
        upper = lower + 1
        fraction = pos - lower
        return sorted_values[lower] + fraction * (sorted_values[upper] - sorted_values[lower])
