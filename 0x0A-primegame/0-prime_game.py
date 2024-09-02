#!/usr/bin/python3


def isWinner(x, nums):
    """
    main func
    """
    if x < 1 or not nums:
        return None

    max_num = max(nums)
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for j in range(i*i, max_num + 1, i):
                primes[j] = False

    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1

    if maria_wins * 2 == x:
        return None
    if maria_wins * 2 > x:
        return "Maria"
    return "Ben"
