#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Docstring explaining what each arguments mean.

    Args:
        wink (str): Arg to be multiplied by numwink.
        numwink (int): Arg to be multiplied by wink and 'nudge'.

    Returns:
         str: ALl arguments are returned with a question, winks and nudges.

    Examples:

        >>> Know_what_i_mean('wink', 3)
        'Know what I mean? winkwinkwink, nudge nudge nudge'

        >>> Know_what_i_mean('yea', 3)
        'Know what I mean? yeayeayea, nudge nudge nudge'

    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
