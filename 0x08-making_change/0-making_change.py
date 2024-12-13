#!/usr/bin/python3
""" This module defines the makeChange function
"""
import sys


def makeChange(coins, total):
    """ This function calculates the fewest number of coins
    needed to meet a given amount total
    Args:
        coins: list of the values of the coins
        total: amount
    Returns:
        fewest number of coins needed to meet total
    """
    n = len(coins)
    if total <= 0:
        return 0
    ans = []
    i = n - 1
    while (i >= 0):
        while (total >= coins[i]):
            total -= coins[i]
            ans.append(coins[i])
        i -= 1
    if total != 0:
        return -1
    return len(ans)
    # table = [0 for i in range(total + 1)]
    # table[0] = 0
    # # initializing the table with infinite values
    # for i in range(1, total + 1):
    #     table[i] = sys.maxsize
    # # compute minimum coins required
    # for i in range(1, total + 1):
    #     # go through smaller coins solutions
    #     for j in range(n):
    #         if (coins[j] <= i):
    #             sub_res = table[i - coins[j]]
    #             if sub_res != sys.maxsize and sub_res + 1 < table[i]:
    #                 table[i] = sub_res + 1
    # if table[total] == sys.maxsize:
    #     return -1
    # return table[total]
