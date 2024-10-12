#!/usr/bin/python3
'''A simple script that print a Pascal triangle'''


def pascal_triangle(n):
    '''A function that create Pascal trianle
    Parameters:
    -----------
        n: integer
            - represent the height of Pascal triangle
    Return:
    -------
        list of list representing the Pascal triangle numbers
    '''
    if n <= 0:
        return []
    p = [[1] for i in range(n)]
    for a in range(1, n):
        for i in range(a, n):
            if i == a:
                p[i].append(1)
            else:
                p[i].append(p[i-1][-1]+p[i-1][-2])
    return p
