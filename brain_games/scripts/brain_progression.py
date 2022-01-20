#!/usr/bin/env python
"""Main module for progression game."""
from typing import Union

from brain_games.cli import welcome_user
from brain_games.game import start_game


def main() -> None:
    """Run progression game."""
    username: Union[str, None] = welcome_user()
    start_game('progression', username)


if __name__ == '__main__':
    main()
