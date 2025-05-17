#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    total = 0
    previous = 0

    for char in reversed(roman_string):
        if char == 'M':
            value = 1000
        elif char == 'D':
            value = 500
        elif char == 'C':
            value = 100
        elif char == 'L':
            value = 50
        elif char == 'X':
            value = 10
        elif char == 'V':
            value = 5
        elif char == 'I':
            value = 1
        else:
            return 0

        if value >= previous:
            total += value
        else:
            total -= value

        previous = value

    return total
