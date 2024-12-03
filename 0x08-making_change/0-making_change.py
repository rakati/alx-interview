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
    coins.sort()
    dp = [[0] * (total + 1) for _ in range(len(coins))]

    for i in range(len(coins) - 1, -1, -1):
        for sub_total in range(1, total + 1):
            dp[i][sub_total] = float("inf")
            take = float("inf")
            notake = float("inf")

            # case of taking the current coin i
            if sub_total - coins[i] >= 0:
                take = dp[i][sub_total - coins[i]]
                if take != float("inf"):
                    take += 1
            # case of not taking the current coin
            if i + 1 < len(coins):
                notake = dp[i + 1][sub_total]

            dp[i][sub_total] = min(take, notake)

    return dp[0][total] if dp[0][total] != float("inf") else -1
