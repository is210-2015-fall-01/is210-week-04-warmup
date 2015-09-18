#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """ Returns a str and does math to repeat certain words.

    Args:
        wink (str): Arg to doubled by numink arg.
        numwink (int): Arg that returns a 2 to double the wink arg.

    Returns:
        str: both args + 'Know what I mean?' str. Removes space between
        the repeated argument of 'wink.'

    Examples:
    
        >>> know_what_i_mean(winks)
        'Know what I mean? winkswinks, nudge nudge'
    """
    
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr

MYVAR = know_what_i_mean('winks')
print MYVAR
