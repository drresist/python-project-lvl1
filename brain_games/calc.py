"""Define functions for calc game."""

import random
from datetime import datetime

VARIANTS = ('*', '+', '-')


def setup_task() -> str:
    """Return task message.

    Args:

    Returns:
        return task text
    """
    return 'What is the result of the expression?'


def calc_expression_generator() -> tuple:
    """Generate expression for question and answer.

    Args:

    Returns:
        tuple of (expression, answer, task)
    """
    random.seed(datetime.now())
    first_number: int = random.randint(1, 100)
    second_number: int = random.randint(1, 100)
    action: str = random.choice(VARIANTS)
    expression: str = '{0} {1} {2}'.format(first_number, action, second_number)
    answer: int = 0
    if action == '*':
        answer = first_number * second_number
    if action == '+':
        answer = first_number + second_number
    if action == '-':
        answer = first_number - second_number
    return (expression, str(answer), setup_task())
