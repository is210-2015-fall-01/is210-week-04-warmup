#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Showcase string functions and return a string.

    Args:
        wink(str): Arg to be repeated by numwink times.
        numwink(int): Just a random integer number. Default: 2.

    Returns:
        str: Built_in string functions put arguments together and form a string.

    Examples:

        >>> know_what_i_mean('wink', 3)
        'Know what I mean? winkwinkwink, nudge nudge nudge'

        >>> know_what_i_mean('5', 5)
        'Know what I mean? 55555, nudge nudge nudge nudge nudge'
    """
        
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
