#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """This function does some multiplication and combines two variables into a
    string.

    Args:
        wink (string):  Arg to be multiplied with numwink
        numwink (int, optional): Arg to multiply wink.  Default: 2

    Returns:
        str: Takes a string and multiplies it by 2 or the the number
        chosen by the user.

    Examples:

        >>> know_what_i_mean('do ya?', 4)
        'Know what I mean? do ya?do ya?do ya?, nudge nudge nudge'

        >>> know_what_i_mean('wink ')
        'Know what I mean? wink wink, nudge nudge'

        >>> know_what_i_mean('wink ', 5)
        'Know what I mean? wink wink wink wink wink, nudge nudge nudge nudge
        nudge'
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
