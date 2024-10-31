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
        # check only least 8 significant bits
        code = code & 0xFF
        if n > 0:
            if code >> 6 != 0b10:
                return False
            n -= 1
        else:
            # not expecting continuation bytes
            if code >> 7 == 0:
                n = 0
            elif code >> 5 == 0b110:
                # should expect one continuation byte
                n = 1
            elif code >> 4 == 0b1110:
                # should expect two continuation bytes
                n = 2
            elif code >> 3 == 0b11110:
                # should expect three continuation bytes
                n = 3
            else:
                # format unknown
                return False
    return n == 0
