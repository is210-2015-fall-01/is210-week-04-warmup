#!/usr/bin/env python
# -*- coding: utf-8 -*
"""Set a default value in our function definition"""


def defaults(my_required, my_optional=True):
    """The two parameters.

  Args:
       my_required: First parameter, without any default value.
       my_optional: Second parameter, with a boolean value.

    Returns:
       A boolean value, True if successful,False if otherwise.

    Examples:
        >>> defaults(True)
        True
       >>> defaults(True, False)
       False
       >>> defaults(False,False)
        True
   """
    return my_optional is my_required
