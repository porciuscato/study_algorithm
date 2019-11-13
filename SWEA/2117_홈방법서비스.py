import sys

sys.stdin = open('2117.txt', 'r')

for T in range(1, int(input())+ 1):
    mx = 0
    houses = []
    N, M = map(int, input().split())
    for row in range(N):
        info = list(map(int, input().split()))
        for col in range(N):
            if info[col]:
                houses.append((row, col))
    for row in range(N):
        for col in range(N):
            distance = []
            for house in houses:
                distance.append(abs(row - house[0]) + abs(col - house[1]))
            for K in range(1, 2 * N + 1):
                price = (K * K) + ((K - 1) * (K - 1))
                count = 0
                for dis in distance:
                    if dis < K:
                        count += 1
                if (M * count) - price >= 0 and count > mx:
                    mx = count
    print('#{} {}'.format(T, mx))