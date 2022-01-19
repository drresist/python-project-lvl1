"""Template game logic."""


from typing import Union

from brain_games.calc import calc_expression_generator
from brain_games.even import even_variants_generator


def start_game(gamename: str = "even", username: Union[str, None] = "") -> None:
    """Start game.

    Args:
        gamename (str): what game will be started
    Returns:
    """
    task: str = ""
    answer: str = ""
    question: str = ""
    win_counter: int = 0

    if gamename == "even":
        func = even_variants_generator
    elif gamename == "calc":
        func = calc_expression_generator
    else:
        func = even_variants_generator
    question, answer, task = func()
    print(task)
    while True:
        if win_counter == 3:
            print("Congratulations, {0}!".format(username))
            break
        print("Question: {0}".format(question))
        user_answer = input("Your answer: ")
        if user_answer == answer:
            print("Correct!")
            win_counter += 1
            question, answer, task = func()
            continue
        if user_answer != answer:
            print(
                "'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(
                    user_answer, answer
                )
            )
            break
