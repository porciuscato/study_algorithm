N = int(input())
data = []
DP = [[0] * N for _ in range(N)]
for i in range(1, N + 1):
    data.append(list(map(int, input().split())) + ([0] * (N - i)))

DP[0] = data[0]
for idx in range(1, N):
    for jdx in range(idx + 1):
        if jdx == 0:
            DP[idx][jdx] = data[idx][jdx] + DP[idx - 1][jdx]
        elif jdx == idx:
            DP[idx][jdx] = data[idx][jdx] + DP[idx - 1][jdx - 1]
        else:
            DP[idx][jdx] = data[idx][jdx] + max(DP[idx - 1][jdx], DP[idx - 1][jdx - 1])

print(max(DP[N - 1]))
