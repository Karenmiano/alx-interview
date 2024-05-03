#!/usr/bin/python3
"""
Defines canUnlockAll function
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened

    Args:
        boxes: A list of lists where the the inner list is a
                box containing keys

    Returns:
        True if all boxes can be opened, else False
    """
    keys = set()
    not_opened = []

    for index, box in enumerate(boxes):
        if index not in keys and index != 0:
            not_opened.append(index)
        else:
            keys.update(box)
            keys.discard(index)

    for index in not_opened:
        if index not in keys:
            return False
        keys.update(boxes[index])

    return True
