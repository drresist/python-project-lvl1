#!/usr/bin/env python
from typing import Union
from brain_games.cli import welcome_user
from brain_games.game import start_game


def main() -> None:
    username: Union[str, None] = welcome_user()
    start_game("even", username)


if __name__ == "__main__":
    main()
