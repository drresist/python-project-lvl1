#!/usr/bin/env python
"""Main script module for EvenGame."""
from typing import Union

from brain_games.cli import welcome_user
from brain_games.games.game import start_game


def main() -> None:
    """Init even game logic."""
    username: Union[str, None] = welcome_user()
    start_game('even', username)


if __name__ == '__main__':
    main()
