#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module is for task_05."""


def defaults(my_required, my_optional=True):
    """This is function which compares to boolean values.

    This fuctions compares two boolean values which are supplied as arguments.
    The second value is optional.

    Args:
        my_optional (boolean, optional): A boolean value
        my_required (boolean): Another boolean value

    Returns:
        A boolean value.

    Example:
        >>> defaults(False)
        False
    """
    return my_optional is my_required
