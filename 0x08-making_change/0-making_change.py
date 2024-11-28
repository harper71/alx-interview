#!/usr/bin/python3
"""make changes"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins
    needed to meet a given amount total.

    Args:
        coins (list): List of coin denominations.
        total (int): The target amount.

    Returns:
        int: The fewest number of coins needed to meet total.
             If total is 0 or less, return 0.
             If total cannot be met by any
             number of coins, return -1.
    """

    if total <= 0:
        return 0

    # Initialize the DP array with a large value (representing infinity)
    dp = [float('inf')] * (total + 1)
    # Base case: 0 coins needed to make a total of 0
    dp[0] = 0

    # Loop through each coin denomination
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
