#!/usr/bin/env python
"""Main programm."""

from brain_games.cli import welcome_user


def brain_games():
    """Greet user."""
    print('Welcome to the Brain Games!')


def main():
    """Make user inteface."""
    brain_games()
    welcome_user()


if __name__ == '__main__':
    main()
