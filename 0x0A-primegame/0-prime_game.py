#!/usr/bin/python3
""" This module defines the isWinner function """


def sieve_of_eratosthenes(max_n):
    """ Precompute primes up to max_n using Sieve of Eratosthenes """
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, max_n + 1, i):
                is_prime[multiple] = False
    return is_prime


def isWinner(x, nums):
    """ This function determines the winner of the primeGame
    either Ben or Maria based on the rounds played.
    Args:
        x (int): number of rounds
        nums (list): list of numbers
    """
    if x <= 0 or not nums:
        return None

    max_n = max(nums)  # Find the largest number in the rounds
    # Precompute primes up to the largest number
    primes = sieve_of_eratosthenes(max_n)

    # Initialize win counters
    maria_wins = 0
    ben_wins = 0

    # Loop through each round
    for n in nums:
        # Simulate game with the number n
        # Numbers from 1 to n are available initially
        available_numbers = [True] * (n + 1)
        moves = 0
        for i in range(2, n + 1):
            if available_numbers[i] and primes[i]:
                # If the number is prime and still available, it's a valid move
                moves += 1
                # Mark all multiples of the prime number as unavailable
                for multiple in range(i, n + 1, i):
                    available_numbers[multiple] = False

        # Determine who wins the round based on the number of moves
        if moves % 2 == 0:
            ben_wins += 1  # Ben wins if the number of moves is even
        else:
            maria_wins += 1  # Maria wins if the number of moves is odd

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
