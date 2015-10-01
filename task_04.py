#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Defining a function with three parameters"""


def too_many_kittens(kittens, litterboxes, catfood):
    """Declares three parameters.

    Args:
        kittens(mixed): First parameter denoting number of kittens
        litterboxes(int): a parameter defining number of available litterboxes.
        catfood(bool): denoting if there is any catfood.

    Returns:
        a boolean, True if successful, False if otherwise.

    Examples:
        >>> too_many_kittens(12, 12, False)
        True
        >>> too_many_kittens(13, 12, True)
        True
        >>> too_many_kittens(12, 13, True)
        False
    """

    return not(litterboxes >= kittens and catfood)
