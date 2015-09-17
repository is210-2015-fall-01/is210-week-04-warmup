#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Checks whether kitttens have enough food."""


def too_many_kittens(kittens, litterboxes, catfood):
    """Ensures we have at least one litterbox for each kitten and that we have
    some catfood. It then uses inversion via not to answer whether or not we
    have too many kittens.

    Args:
        kittens: number of kittens
        litterboxes: integer number of available litterboxes
        catfood: boolean representing True if catfood exists; else, False.

    Returns:
        True or False
        For Example: too_many_kittens(5, 15, True) returns False

    Raises:
        TypeError: too_many_kittens() takes exactly 3 arguments
    """
    return not (litterboxes >= kittens and catfood)
