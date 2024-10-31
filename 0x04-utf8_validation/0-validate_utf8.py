#!/usr/bin/python3
'''A simple script that check if the given data are a valid UTF-8 character'''


def validUTF8(data):
    '''A function that check if the given list of data are valid UTF-8.
    Parameters:
    -----------
        data: list
            - list of integers representing encoded characters.
    Return:
    -------
        True if all integers of data list are valid utf-8 otherwise False
    '''
    # counting number of continuation bytes to be fulfilled
    n = 0
    for code in data:
        if n == 0:
            # not expecting continuation bytes
            if code >> 7 == 0:
                continue
            elif code >> 5 == 0b110:
                n = 1
            elif code >> 4 == 0b1110:
                n = 2
            elif code >> 3 == 0b11110:
                n = 3
            else:
                return False
        elif n > 0:
            if n >> 6 != 0b10:
                return False
            n -= 1
    return True if n == 0 else False
