"""Command line interface for brain-games."""


import prompt


def welcome_user() -> None:
    """Read username from input and print welcome message."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
