#!user/bin/env python
# -*- coding: utf-8 -*-
"""Module that tests to see if parameters are the same"""


def defaults(my_required, my_optional=True):
    """Module compares the two integers.

    Args:
      my_optional (mixed): first parameter to compare
      my_required (mixed): sexond parameter to compare

    Returns:
        A bool value indicating whether or not the two parameters are the same.

    Examples:
         defaults(True, False)

         >>>'False'

         defaults(True)
         >>>'True'
    """
    defaults_val = my_optional is my_required

    return defaults_val


print defaults(True, False)
