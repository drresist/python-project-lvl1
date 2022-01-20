"""Template game logic."""

from typing import Union

from brain_games.games.calc import calc_expression_generator
from brain_games.games.even import even_variants_generator
from brain_games.games.gcd import gcd_generator
from brain_games.games.prime import prime_generator
from brain_games.games.progression import progression_generator


def choose_game(gamename: str) -> callable:
    """Choose game using gamename.

    Args:
        gamename (str): type of game

    Returns:
        return generator function
    """
    games = {
        'even': even_variants_generator,
        'calc': calc_expression_generator,
        'gcd': gcd_generator,
        'progression': progression_generator,
        'prime': prime_generator,
    }
    return games[gamename]


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
