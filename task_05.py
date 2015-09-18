#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a simple module that compares two values."""

def defaults(my_required, my_optional=True):
    """This function compares a value to another value using a logical
    comparison.

    Args:
        my_required (mixed): Arg to be logically compared to my_optional.
        my_optional (mixed, optional): Arg logically compared to my_required.
        Default: True.

    Returns:
        bool: The two arguements compared to each other.

    Examples:

        >>> defaults(1, 2)
        False

        >>> defaults(3, 3)
        True

        >>> defaults('string', 'string')
        True

        >>> defaults('string', 'difstring')
        False

        >>> defaults(True)
        True

        >>> defaults(2+2, 1+3)
        True
    """
    answer = my_optional is my_required
    return answer
