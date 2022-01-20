"""Generate task for Progression game."""
import datetime
import random

random.seed(datetime.datetime.now())


def create_arithmetic_progression() -> list:
    """Create arithmetic progression.

    Returns:
        list of progression
    """
    current_value = random.randint(1, 5)
    diff = random.randint(2, 5)
    progression_len = random.randint(7, 10)
    task: list = []
    for _ in range(0, progression_len):
        task.append(current_value)
        current_value += diff
    return task


def progression_generator() -> tuple:
    """Create tuple with task for user.

    Returns:
        tuple with (question, answer, task)
    """
    question_list: list = create_arithmetic_progression()
    task: str = 'What number is missing in the progression?'
    answer: str = str(random.choice(question_list[1:-1]))
    question: str = ' '.join([str(number) for number in question_list])
    return question.replace(' {0} '.format(answer), ' .. '), answer, task
