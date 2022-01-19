"""Command line interface for brain-games."""


import prompt


def welcome_user() -> str | None:
    """Read username from input and print welcome message."""
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {0}!".format(name))
    return name
