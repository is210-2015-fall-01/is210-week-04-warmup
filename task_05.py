#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setting a default value in our function definition."""


def defaults(my_required, my_optional=True):
    """Compares the two values  to see if they equal one another.

    Args:
        my_optional (bol): first comparison arg value set to true as default.
        my_required (mixed): second comparison arg value to be typed in.

    Returns:
        bool: (true, false) depending on the paramaters entered.

    Examples:
        >>> defaults(True)
        True

        >>> defaults(True, False)
        False

        >>> defaults(False, False)
        True
    """
    return my_optional is my_required
