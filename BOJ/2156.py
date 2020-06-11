import sys

sys.stdin = open("2156.txt")


def main():
    N = int(input())
    DP = [[0 for _ in range(N + 1)] for __ in range(3)]
    for i in range(1, N + 1):
        DP[0][i] = int(input())
    DP[1][1] = DP[0][1]
    try:
        DP[1][2] = DP[0][2]
        DP[2][2] = DP[1][1] + DP[0][2]
    except IndexError:
        return DP[0][1]
    for j in range(3, N + 1):
        DP[1][j] = max(max(DP[1][j - 2], DP[2][j - 2]), max(DP[1][j - 3], DP[2][j - 3])) + DP[0][j]
        DP[2][j] = DP[1][j - 1] + DP[0][j]
    return max(max(DP[1]), max(DP[2]))


print(main())
