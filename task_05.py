#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 05"""


def defaults(my_required, my_optional=True):
    """Docstring explaining what each arguments mean.

    Args:
        my_required (bool): Arg has no defaults.
        my_optional (bool): Arg has a value of 'True'.

    Returns:
        (bool): Arguments returns a boolean.

    Examples:
        >>> defaults(True)
        True

        >>> defaults(True, False)
        False
    """
    return my_optional is my_required
