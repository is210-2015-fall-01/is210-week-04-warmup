#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module is for task_04."""


def too_many_kittens(kittens, litterboxes, catfood):
    """This is a kittens function.

    This fuctions ensure that we don't have more kittens than litterboxes.
    It also takes into account if we have any catfoot. If there is no catfood
    and there is not at least one litterbox per kittens, then we have too many
    kittens.

    Args:
        kittens (mixed): The number of kittens.
        litterboxes (mixed): The number of litterboxes.
        catfood (boolean): Cat food presents.

    Returns:
        A boolean value.

    Example:
        >>> too_many_kittens(2, 3, False)
        True
    """
    return not (litterboxes >= kittens and catfood)
