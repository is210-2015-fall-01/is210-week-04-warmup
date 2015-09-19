#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""There many be way too many kittens."""


def too_many_kittens(kittens, litterboxes, catfood):
    """This function finds out if we have at least one litter box for each
    kitten and some catfood.

    Args:
        kittens(int, optional): number of kittens
        litterboxes(int): number of available litterboxes
        catfood(bool): whether or not any catfood exists
    Returns:
        True or False on whether we have too many kittens,

    Examples:

        >>>too_many_kittens(12, 12, False)
        True
    """
    return not (litterboxes >= kittens and catfood)
