# I got help from ChatGPT
import math
import random


def simulate_gravel_sizes(supplier, n=100):
    """
    Simulates n gravel sizes for a supplier, based on their screening process.

    Parameters:
    - supplier: Identifier for the supplier ('A' or 'B').
    - n: Number of gravel sizes to simulate.

    Returns:
    A list of simulated gravel sizes.
    """
    if supplier == 'A':
        # Supplier A: Sizes between 3/8" and 1"
        min_size, max_size = 3 / 8, 1
    else:
        # Supplier B: Sizes up to 7/8"
        min_size, max_size = 3 / 8, 7 / 8

    return [random.uniform(min_size, max_size) for _ in range(n)]


def calculate_mean(data):
    """Calculates the mean of the given data."""
    return sum(data) / len(data)





def simpsons_rule(f, a, b, n):
    """
    Numerically integrates f from a to b using Simpson's 1/3 rule with n intervals.

    Parameters:
    - f: The function to integrate.
    - a, b: The interval to integrate over.
    - n: The number of intervals (must be even).

    Returns:
    The estimated integral of f from a to b.
    """
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(xi) for xi in x]
    return (h / 3) * (y[0] + 4 * sum(y[i] for i in range(1, n, 2)) + 2 * sum(y[i] for i in range(2, n, 2)) + y[n])


