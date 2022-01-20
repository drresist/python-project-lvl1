#!/usr/bin/env python
"""Main moudle for calc game."""
from typing import Union

from brain_games.cli import welcome_user
from brain_games.game import start_game


def main() -> None:
    """Run calc game."""
    username: Union[str, None] = welcome_user()
    start_game('calc', username)


if __name__ == '__main__':
    main()
