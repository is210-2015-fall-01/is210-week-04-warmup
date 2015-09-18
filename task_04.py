#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""In this task, you'll be defining a function with three parameters."""

def too_many_kittens(kittens, litterboxes, catfood):
    """Does some math and ensures we have enough supplies

    Args:
        kittens (int): Arg to tell us number of kittens we have.
        litterboxes (int): Arg to tell us Number of litterboxes on hand.
        catfood (bool): Arg that represents wether or not any catfood exists.

    Returns:
        bool: If arg is eihter true or false depending on declaration values.

    Examples:

        >>> too_many_kittens(12, 12, False)
        True

        >>> too_many_kittens(13, 12, True)
        True

        >>> too_many_kittens(12, 13, True)
        False
    """
    return not (litterboxes >= kittens and catfood)
