#!user/bin/env python
# -*- coding: utf-8 -*-
"""Module that tests to see if there are enough litterboxes"""


def too_many_kittens(kittens, litterboxes, catfood):
    """ Returns two integers and boolean to ensure that there enough litterboxes
        for all of the cats.

    Args:
        kittens (int): Number of kittens.
        litterboxes (int): Number of litterboxes.
        cafood (bool): At least some catfood? True or False.

    Returns:
        A bool value indicating whether or not there are enough litterboxes
        for all of the kittens and at least some catfood.

    Examples:
         too_many_kittens(4, 5, True)

         >>>'False'
    """
    cats = not (litterboxes >= kittens and catfood)

    return cats


print too_many_kittens(4, 5, True)
