"""Generate task for Prime game."""
import datetime
import random

random.seed(datetime.datetime.now())


def is_prime(num: int) -> str:
    """Check if number is prime.

    Args:
        num (int): number to check

    Returns:
        str 'yes' or 'no'
    """
    div_counter = 0
    for numbers in range(1, num + 1):
        if num % numbers == 0:
            div_counter += 1
    if div_counter > 2:
        return 'no'
    return 'yes'


def prime_generator() -> tuple:
    """Generate task for Prime game.

    Returns:
        tuple of (question, answer, task)
    """
    question_number: int = random.randint(1, 100)
    answer: str = is_prime(question_number)
    return question_number, answer, 'Answer "yes" if given number is prime. Otherwise answer "no".'
