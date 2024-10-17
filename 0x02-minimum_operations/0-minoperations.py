#!/usr/bin/python3
'''A simple script that calculate number of operations to certain number of
copy of a character using only `copy all` and `past` operator.'''


def minOperations(n):
    '''A function that calculate minimum number of operations to have n
    copy of a character using two operation `copy all` and `past`.
    Parameters:
    -----------
        n: int
            - Number of characters to form using copy past.
    Return:
    -------
        minimum number of operations otherwise 0 if not possible.
    '''
    op = 0
    if n < 1:
        return op
    while n % 2 == 0:
        op += 2
        n /= 2
    d = 3
    while d * d <= n:
        while n % d == 0:
            op += d
            n /= d
        d += 2
    if n > 1:
        op += n
    return int(op)
