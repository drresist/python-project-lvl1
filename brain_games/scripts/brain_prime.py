#!/usr/bin/env python
"""Main module for Prime game."""
from typing import Union

from brain_games.cli import welcome_user
from brain_games.games.game import start_game


def main() -> None:
    """Run Prime game."""
    username: Union[str, None] = welcome_user()
    start_game('prime', username)


if __name__ == '__main__':
    main()
