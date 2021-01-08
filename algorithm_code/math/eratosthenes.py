def prime_numbers(number):
    sieve = [True] * (number + 1)
    sqroot = int(number ** 0.5)
    for i in range(2, sqroot + 1):
        if sieve[i]:
            for j in range(i + i, number + 1, i):
                sieve[j] = False
    return [t for t in range(2, number + 1) if sieve[t]]


size = 10000000
print(prime_numbers(size))
