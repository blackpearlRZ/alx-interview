#!/usr/bin/python3
"""This module defines the canUnlockAll function
"""


def canUnlockAll(boxes):
    """ this function defines the solution for the lockboxes
    each interview problem
    Args;
        boxes (list): List of lists representing a box with each
        box containing keys.
    Returns:
        True - if all boxes can be unlocked.
        False - if not all boxes can be unlocked.
    """

    # Opening first box
    openedBoxes = [0]

    # Adding keys in first box to key roster
    keys = []
    for key in boxes[0]:
        keys.append(key)

    # Append keys and add opened boxes
    while keys:
        key = keys.pop()
        if key < len(boxes):
            if key not in openedBoxes:
                openedBoxes.append(key)
                for newKey in boxes[key]:
                    keys.append(newKey)

    # Compare lens of opened boxes to the boxes
    if (len(boxes) == len(openedBoxes)):
        return True
    else:
        return False
