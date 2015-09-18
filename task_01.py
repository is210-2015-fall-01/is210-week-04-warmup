#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Displays wink string a specified number of times

    Args:
        wink(mixed): Arg to be repeated inputed by user
        numwink(int): Arg that displays wink a defined # of time 2 is default.

    Returns:
        Str: Displays the wink, numwink, using string function.

    Examples:

        >>> know_what_i_mean('jellybean', 2)
        'Know what I mean? jellybeanjellybean, nudge nudge'

        >>> know_what_i_mean('mein freund', 1)
        'Know what I mean? mein freund, nudge'
        
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
