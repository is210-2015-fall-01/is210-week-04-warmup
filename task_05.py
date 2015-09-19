#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module does some pretty crazy math."""


def defaults(my_required, my_optional=True):
    """This function tests that the default matches the correct parameters.

    Args:
        myrequired(book): This is the parameter that will not have any default.
        my_optional(bool): This parameter has the default, in this case T.

    Returns:
        bool: Whether the two parameters are the same.

    Examples:

        >>> defaults(True)
        True
        >>> defaults(True, False)
        False
    """
    return my_optional is my_required
