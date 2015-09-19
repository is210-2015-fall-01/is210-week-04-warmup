#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Prints a statement followed by another dynamically built phrase.

    This function prints 'Know what I mean?', followed by a series of winks
    and nudges. It accepts two arguments  and multiplies both arguments by
    the second (optional) argument to construct the phrase.

    Args:
        wink (str): Any string that would signify a wink.
        numwink (int, optional): a integer to serve as the multiplier.

    Returns:
        The sentense 'Know what I mean?' followed by the first argument and
        the string 'nudge' multiplied by numwin or the defaulf valye (2).

    Example:
        >>> know_what_i_mean('wink', 3)
        'Know what I mean? winkwinkwink, nudge nudge nudge'
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
