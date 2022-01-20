"""Define functions for evenOrNot game."""

import random
from datetime import datetime


def is_even(num: int) -> bool:
    """Check that number is even.

    Args:
        num (int): random number for checking

    Returns:
        true or false
    """
    return num % 2 == 0


def even_variants_generator() -> tuple:
    """Generate random number and answer for game.

    Args:

    Returns:
        tuple of (random num, answer, task)
    """
    random.seed(datetime.now())
    random_number: int = random.randint(1, 100)
    task: str = 'Answer "yes" if the number is even, otherwise answer "no".'
    answer: str = ''
    if is_even(random_number):
        answer = 'yes'
    if not is_even(random_number):
        answer = 'no'
    return random_number, answer, task
