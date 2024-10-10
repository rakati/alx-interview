#!/usr/bin/python3
'''A simple script that check if a graph is connected'''


def canUnlockAll(boxes):
    '''A function that check if boxes are unlocked
    Parameters:
    -----------
        boxes: list
            - list of list aka list of box on each box list of keys.
            - box 0 is always unlocked
    Return:
    -------
        True if all boxes can be unlocked otherwise False
    '''
    from collections import deque

    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    unlocked = set([0])
    queue = deque([0])

    while queue:
        current_box = queue.popleft()
        for key in boxes[current_box]:
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)
                queue.append(key)
    return len(unlocked) == len(boxes)
