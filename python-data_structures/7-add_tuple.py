#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = ()

    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0,) * (2 - len(tuple_a))
        # (2 - len(tuple_a)) - calculates how many more
        # elements needed to make a tuple of 2
        # (0,) * (2 - len(tuple_a)) - creates a tuple of 0s,
        # repeating as many times as needed
    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0,) * (2 - len(tuple_b))
    if len(tuple_a) > 2:
        tuple_a = tuple_a[0:2]
    if len(tuple_b) > 2:
        tuple_b = tuple_b[0:2]

    for i in range(len(tuple_a)):
        result += (tuple_a[i] + tuple_b[i],)
    return result
