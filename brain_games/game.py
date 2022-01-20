"""Template game logic."""

from typing import Callable, Union

from brain_games.calc import calc_expression_generator
from brain_games.even import even_variants_generator
from brain_games.gcd import gcd_generator
from brain_games.progression import progression_generator


def choose_game(gamename: str) -> Callable:
    """Choose game using gamename.

    Args:
        gamename (str): type of game

    Returns:
        return generator function
    """
    if gamename == 'even':
        func = even_variants_generator
    elif gamename == 'calc':
        func = calc_expression_generator
    elif gamename == 'gcd':
        func = gcd_generator
    elif gamename == 'progression':
        func = progression_generator
    else:
        func = even_variants_generator

    return func


def win_condition(counter: int, username: Union[str, None]) -> bool:
    """Check win condition.

    Args:
        counter (int): count rounds to win. Strict 3 = win
        username (str): username for congratulations :)

    Returns:
        win or not
    """
    if counter == 3:
        print('Congratulations, {0}!'.format(username))
        return True
    return False


def start_game(gamename: str = 'even', username: Union[str, None] = '') -> None:
    """Run basic game logic accross all games.

    Args:
        gamename (str): what game will be started
        username (Union[str,None]): user name
    """
    task: str = ''
    answer: str = ''
    question: str = ''
    win_counter: int = 0
    func = choose_game(gamename)
    question, answer, task = func()
    print(task)
    while True:
        if win_condition(win_counter, username):
            break
        print('Question: {0}'.format(question))
        user_answer = input('Your answer: ')
        if user_answer == answer:
            print('Correct!')
            win_counter += 1
            question, answer, task = func()
            continue
        if user_answer != answer:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(user_answer, answer))
            break
