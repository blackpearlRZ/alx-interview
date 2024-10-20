#!/usr/bin/python3
""" this module defines the minOperations function
"""


def minOperations(n):
    """ this function returns the fewest number of operations required
        to create n * 'H' characters . the only allowed operations are:
        copy all & Paste
    """
    if n <= 1:
        return 0
    num = n
    divisions = []
    i = 2
    while i <= num:
        if num % i == 0:
            divisions.append(i)
            num = num // i
        else:
            i += 1

    return sum(divisions) if divisions else n
