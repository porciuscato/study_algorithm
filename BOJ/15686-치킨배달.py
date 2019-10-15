import sys

sys.stdin = open('input.txt', 'r')


def solve(arr):
    global ans
    tot = 0
    for house in range(len_house):
        temp = []
        for ar in arr:
            temp.append(data[house][ar])
        tot += min(temp)
        if tot > ans:
            return
    else:
        ans = tot


def combi(arr, depth, last):
    if depth == M:
        solve(arr)
    else:
        for i in range(last, len_store):
            ar = arr[:]
            ar.append(i)
            combi(ar, depth + 1, i + 1)


N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
houses = []
stores = []
for r in range(N):
    for c in range(N):
        if G[r][c] == 1:
            houses.append((r, c))
        elif G[r][c] == 2:
            stores.append((r, c))
len_house = len(houses)
len_store = len(stores)
data = [[0] * len_store for _ in range(len_house)]
for r in range(len_house):
    for c in range(len_store):
        data[r][c] = abs(houses[r][0] - stores[c][0]) + abs(houses[r][1] - stores[c][1])

ans = 1e6
combi([], 0, 0)
print(ans)
