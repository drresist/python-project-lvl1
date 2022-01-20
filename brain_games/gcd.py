"""GCD logic."""

import random
from datetime import datetime


def gcd(first: int, second: int) -> int:
    """Calculate GCD for two numbers.

    Args:
        first (int): first number
        second (int): second number

    Returns:
        return GCD for this numbers
    """
    max_val: int = 1
    for index in range(1, max(first, second)):
        if first % index == 0 and second % index == 0:
            max_val = index
    return max_val


def gcd_generator() -> tuple:
    """Generate random numbers for GCD game.

    Returns:
        tuple of (expression, answer, task)
    """
    random.seed(datetime.now())
    first_number: int = random.randint(1, 100)
    second_number: int = random.randint(1, 100)
    task: str = 'Find the greatest common divisor of given numbers.'
    answer: str = str(gcd(first_number, second_number))
    return '{0} {1}'.format(first_number, second_number), answer, task
