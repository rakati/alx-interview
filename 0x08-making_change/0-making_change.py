#!/usr/bin/python3
"""
A script for solving change making using dynamic programming.
"""


def makeChange(coins, total):
    """find the fewest number of coins needed to meet a given amount of total
    from a pile of coins of different values.

    Args:
        coins (list(int)): list of the positive non null numbers represent
            coins in our possession.
        total (int): positive number represent the amount to achieve using
            given cois.
    Return:
        Fewest number of of coins needed to meet the total.
            - if total is 0 or less return 0
            - if total cannot be met by any number of coins return -1
    """
