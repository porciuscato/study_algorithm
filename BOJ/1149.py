N = int(input())
houses = []
for _ in range(N):
    houses.append(list(map(int, input().split())))

DP = [[0, 0, 0] for _ in range(N)]
DP[0] = houses[0]
for n in range(1, N):
    DP[n][0] = houses[n][0] + min(DP[n - 1][1], DP[n - 1][2])
    DP[n][1] = houses[n][1] + min(DP[n - 1][0], DP[n - 1][2])
    DP[n][2] = houses[n][2] + min(DP[n - 1][0], DP[n - 1][1])
print(min(DP[N - 1]))
