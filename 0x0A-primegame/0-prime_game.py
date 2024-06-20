#!/usr/bin/python3
"""
Prime Game
"""


def count_primes(n):
    """
    Returns number of prime numbers upto n
    """
    prime = [True for i in range(n + 1)]
    p = 2
    num_primes = 0

    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    for p in range(2, n + 1):
        if prime[p]:
            num_primes += 1
    return num_primes


def isWinner(x, nums):
    """
    Returns winner in prime game
    """
    if x < 1 or len(nums) == 0:
        return None

    winner = 'Maria'

    for _ in range(x):
        for n in nums:
            num_primes = count_primes(n)
            if num_primes % 2 == 0:
                winner = 'Ben'
            else:
                winner = 'Maria'

    return winner
