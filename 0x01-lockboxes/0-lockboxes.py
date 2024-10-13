#!/usr/bin/python3
"""Thid module defines the canUnlockAll function
"""


def canUnlockAll(boxes):
    """ this function defines the solution for the lockboxes
    ech interview problem
    Arges;
        boxes (list): List of lists representing a box with each
        box conaining keys.
    Returns:
        True - if all boxes can be unlocked.
        False - if not all boxes can be unlocked.
    """

    openedBoxes = [0]

    keys = []
    for key in boxes[@]:
        keys.append(key)

    while keys:
        key = keys.pop()
        if key < len(boxes):
            if key not in openedBoxes:
                openedBoxes.append(key)
                for newKey in boxes[key]:
                    keys.append(newKey)

    if (len(boxes) == len(openedBoxes)):
        return True
    else:
        return False
