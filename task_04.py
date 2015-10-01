#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 04"""


def too_many_kittens(kittens, litterboxes, catfood):
    """Docstring explaining what each arguments mean.

    Args:
        kittens (int): The number of kittens.
        litterboxes (int): The number of available litterboxes.
        catfood (boolean): Whether or not catfood is present.

    Returns:
        (boolean): Returns 'True' if litterboxes>= kittens and catfood.

    Examples:
        >>> too_many_kittens(12, 12, False)
        True

        >>> too_many_kittens(13, 12, True)
        True

        >>> too_many_kittens(12, 13, True)
        False
    """
    return not (litterboxes >= kittens and catfood)
