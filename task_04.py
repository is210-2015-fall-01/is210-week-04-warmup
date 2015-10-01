#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module determines if you have enough catfood and litterboxes for a
   certain number of kittens."""

def too_many_kittens(kittens, litterboxes, catfood=None):
    """This function combines a boolean and a comparison operation to determine
    if you have to manny kittens.  This statement ensures we have at least one
    litterbox for each kitten and that we have some catfood.

    Args:
        kittens (mixed): Along with catfood, Arg to be compared to litterboxes.
        litterboxes (mixed): Arg to be compared to kittens and catfood.
        catfood (mixed, optional): Arg that is a boolean condition that along
        with litterboxes, is compared to kittens.  Default: None.

    Returns:
        bool: An arguement compared to another arguement along with a boolean
        condition.  If there are too many kittens, it will return True. If there
        are enough items for the number of kittens selected, it will return
        False.
        

    Examples:

        >>> too_many_kittens(14, 12, True)
        True

        >>> too_many_kittens(12, 12, True)
        False

        >>> too_many_kittens(8, 8, False)
        True

        >>> too_many_kittens(6, 6)
        True
    """
    answer = not (litterboxes >= kittens and catfood)
    return answer
