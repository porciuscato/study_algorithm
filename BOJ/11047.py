import sys


def main():
    N, K = map(int, sys.stdin.readline().split())
    coins = [int(sys.stdin.readline()) for _ in range(N)]
    value = K
    idx = N - 1
    ans = 0
    while value != 0:
        if value >= coins[idx]:
            ans += value // coins[idx]
            value %= coins[idx]
        idx -= 1
    print(ans)


main()
