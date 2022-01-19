"""Even game logic."""

import random
from typing import Union
import prompt
from brain_games.cli import welcome_user


def check_answer(user_answer: Union[str, None], right_answer: str) -> str:
    """Check if user right. Return 'yes' or 'no'."""
    if (user_answer == "yes" and right_answer == "yes") or (
        user_answer == "no" and right_answer == "no"
    ):
        return "yes"
    return "no"


def is_even(number: int) -> str:
    """Check that number is even. Return bool."""
    if number % 2 == 0:
        return "yes"
    return "no"


def game() -> None:
    """Game cycle."""
    variants: list[str] = ["yes", "no"]
    correct_counter: int = 0
    username: str | None = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while True:
        num: int = int(random.randint(1, 100))  # generate number
        print("Question: {}".format(num))
        user_answer = prompt.string("Your answer: ")  # read user input
        user_correct: str = check_answer(user_answer, is_even(num))
        if user_correct == "yes":
            correct_counter += 1
            print("Correct!")

        if user_correct == "no" or user_answer not in variants:
            print(
                "'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
                    user_answer, is_even(num)
                )
            )
            print("Let's try again, {0}!".format(username))
            break

        if correct_counter == 3:
            print("Congratulations, {0}".format(username))
            break
