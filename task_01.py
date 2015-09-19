#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Repeats nudges and winks and returns a string.

    Args:
        wink (int): number of times to repeat the 'wink'
        numwick (int): number of times to repeat the 'nudge'

    Returns:
        str: Both arguments possibly repeated following a question.

    Examples:

        >>> know_what_i_mean(2, 5)
        Know what I mean? wink wink nudge nudge nudge nudge nudge'

        >>> know_what_i_mean(4, 3)
        Know what I mean? wink wink wink wink nudge nudge nudge
    """
    winks = ('wink '* wink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
