#!/usr/bin/python3
"""prime number game"""


def isWinner(x, nums):
    """
    Determines the winner of the prime game after x rounds.

    Args:
        x (int): Number of rounds.
        nums (list): Array of n for each round.

    Returns:
        str: Name of the player with the most wins ("Maria" or "Ben").
             Returns None if the winner cannot be determined.
    """

    def sieve(max_n):
        """Precomputes the number of primes up to every
        number ≤ max_n using Sieve of Eratosthenes.
        """
        is_prime = [True] * (max_n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(max_n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_n + 1, i):
                    is_prime[j] = False
        # Compute cumulative prime counts
        prime_count = [0] * (max_n + 1)
        for i in range(1, max_n + 1):
            prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)
        return prime_count

    if x <= 0 or not nums:
        return None

    # Find the maximum n value in nums
    max_n = max(nums)
    # Precompute primes up to max_n
    prime_count = sieve(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # The number of primes up to n
        # determines the number of moves in the game
        moves = prime_count[n]
        # Maria wins if the number of moves is odd
        if moves % 2 == 1:
            maria_wins += 1
        else:
            # Ben wins if the number of moves is even
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
