#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This file is for."""


def defaults(my_required, my_optional=True):
    """Checks to see if two inputs are the same.

    Args:
        my_required: a required param with no default value
        my_optional: default value of True

    Returns:
        True if both arguments are the same or False if they are different
        For Example: defaults(False)returns False & defaults(True, False)
        returns False

    Raises:
        TypeError: defaults() takes at least 1 argument (0 given)
        NameError: name 'x' is not defined
    """
    return my_optional is my_required
