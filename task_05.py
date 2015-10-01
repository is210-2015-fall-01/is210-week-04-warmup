#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This week4 warmup task_05."""


def defaults(my_required, my_optional=True):
    """This function will return boolean values.

    This functions will call boolean values as defined in the passing
    parameters and gives result accordingly.

    Args:
        my_required(boolean): Can be a boolean value.
        my_optional(boolean): This is boolean default is True.

    Returns:
        Returns True if condition is met otherwise returns Falase.

    Example:
        >>> defaults(False)
        False

        >>> defaults(True, False)
        False

        >>> defaults(False, False)
        True

        >>> defaults(True, True)
        True
    """

    return my_optional is my_required
