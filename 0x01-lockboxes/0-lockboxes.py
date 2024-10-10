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
    unlocked = set()

    def dfs(v):
        '''deep first search on all boxes to see if we can visit all of them'''
        unlocked.add(v)
        for key in boxes[v]:
            if key not in unlocked and key < len(boxes):
                dfs(key)

    dfs(0)
    return len(unlocked) == len(boxes)
