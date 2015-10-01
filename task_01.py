#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Defines a function with two parameters.

    Args:
       wink(mixed): First parameter.
        numwink(int): Second parameter, with a  value of 2.

        Returns:
          str: A string because of .format()

           Examples:

             >>>'Know what I mean? (number of)winks, nudges.'


    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
