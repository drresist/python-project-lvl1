"""Command line interface for brain-games."""

from typing import Union

import prompt


def welcome_user() -> Union[str, None]:
    """Print welcome message and request username.

    Args:

    Returns:
        return username
    """
    print('Welcome to the Brain Games!')
    username: Union[str, None] = prompt.string('May I have your name? ')
    print('Hello {0}'.format(username))
    return username
