#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is week4 warmup task_04"""


def too_many_kittens(kittens, litterboxes, catfood):
    """This calls boolean values.

    This function will  ensures that we use boolean values to get true or false
    statement about kittens with their litterboxes and catfood.

    Args:
        kittens(mixed): This parameter is for number of kittens.
        litterboxe(int): This parameter identifies number of litterboxes.
        catfood(boolean): This parameter is boolean values for catfood.

    Returns:
        Returs True if condition is true otherwise returns False.

    Example:
        >>> too_many_kittens(2, 4, False)
        True

        >>> too_many_kittens(10, 3, False)
        True

        >>> too_many_kittens(10, 10, True)
        False

        >>> too_many_kittens(10, 15, True)
        False
    """

    return not (litterboxes >= kittens and catfood)
