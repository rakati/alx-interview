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
    if total == 0 or total < 0:
        return 0
    dp = [float("inf")] * (total + 1)
    dp[0] = 0

    for i in range(len(coins) - 1, -1, -1):
        for j in range(1, total + 1):
            take = float("inf")
            notake = float("inf")

            # If we take coins[i] coin
            if j - coins[i] >= 0:
                take = dp[j - coins[i]]
                if take != float("inf"):
                    take += 1

            if i + 1 < len(coins):
                notake = dp[j]

            dp[j] = min(take, notake)

    return dp[total] if dp[total] != float("inf") else -1
