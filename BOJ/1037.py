def prime_numbers(number):
    sieve = [True] * (number + 1)
    for i in range(2, number):
        if sieve[i]:
            for j in range(i + i, number + 1, i):
                sieve[j] = False
    return [t for t in range(2, number + 1) if sieve[t]]


def get_div(value, primes, huboes):
    hubo = {}
    for prime in primes:
        while value % prime == 0:
            if hubo.get(prime):
                hubo[prime] += 1
            else:
                hubo[prime] = 1
            value //= prime

    for k, v in hubo.items():
        if huboes.get(k):
            huboes[k] = max(huboes[k], v)
        else:
            huboes[k] = v


def main():
    int(input())
    dividers = list(map(int, input().split()))
    huboes = {}
    primes = prime_numbers(max(dividers))
    for div in dividers:
        get_div(div, primes, huboes)

    if len(huboes) == 1:
        for k, v in huboes.items():
            return k ** (v + 1)
    else:
        result = 1
        for k, v in huboes.items():
            result *= (k ** v)
        return result


print(main())
