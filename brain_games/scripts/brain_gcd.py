#!/usr/bin/env python
"""Main moudle for GCD game."""
from typing import Union

from brain_games.cli import welcome_user
from brain_games.game import start_game


def main() -> None:
    """Run gcd game."""
    username: Union[str, None] = welcome_user()
    start_game('gcd', username)


if __name__ == '__main__':
    main()
