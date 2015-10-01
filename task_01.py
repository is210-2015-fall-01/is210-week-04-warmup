#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """This function multiplies string with integers.

    This function will returnstring 'Know what I mean? along with values from
    the arguments.

    Args:
        wink(mixed): This parameter will return values as defined.
        numwink(int, optional): This argument is an integer with default=2.

    Returns:
        str: return argument wink and numwinks as defined.

    Example:
        >>> know_what_i_mean('wink')
        'Know what I mean? winkwink, nudge nudge'

        >>> know_what_i_mean('wink', 1)
        'Know what I mean? wink, nudge'
    """

    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
