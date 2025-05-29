#!/usr/bin/python3
def add_integer(a, b=98):
    """ Return an the addition of a and b.

    Args:
        a (int or float): First number to add
        b (int or float, optional): Second number to add. Defaults to 98.

    Raises:
        TypeError: If either a or b is not an integer or float.

    Returns:
        int: the sum of a and b converted to an int.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
