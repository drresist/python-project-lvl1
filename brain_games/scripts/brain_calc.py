#!/usr/bin/env python
from typing import Union
from brain_games.game import start_game
from brain_games.cli import welcome_user


def main() -> None:
    username: Union[str, None] = welcome_user()
    start_game("calc", username)


if __name__ == "__main__":
    main()
