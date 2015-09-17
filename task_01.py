#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Receives a string and numerical input from the user then repeatedly
    prints the string.

    Args:
        wink: a string to be repeated
        numwink: the number of times to repeat the string

    Returns:
        A string that results from the concatenation of (a) the input string
        repeated numwink times & then stripped of leading and trailing
        whitespace, followed by (b) the word nudge repeated numwink times &
        then stripped of leading and trailing whitespace.

        For example: know_what_i_mean(' _  I ~  ', 3) returns
        'Know what I mean? _  I ~   _  I ~   _  I ~, nudge nudge nudge'
    Raises:
        NameError: name 'x' is not defined (two arguments-a string and a number
        -must be entered)
        AttributeError: 'int' object has no attribute 'strip' (two arguments
        -a string and a number-must be entered)
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
