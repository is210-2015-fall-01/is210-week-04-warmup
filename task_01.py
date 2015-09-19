#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """This function gets two inputs and returns a string and displays winks.

    Args:
        wink (mixed): this will get repeated
        numwick (int): number of times to repeat the 'nudge'

    Returns:
        str: Both arguments possibly repeated following a question.

    Examples:

        >>> know_what_i_mean('Wow', 5)
        'Know what I mean? wink wink nudge nudge nudge nudge nudge'
        >>> know_what_i_mean('NO', 3)
        'Know what I mean? NONONO, nudge nudge nudge'
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
