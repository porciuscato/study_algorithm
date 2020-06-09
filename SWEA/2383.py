import sys

sys.stdin = open("2383.txt", "r")


def solve2(arr, inj):
    if len(arr):
        depth = stairs[inj][2]
        table = [0] * 200
        for num in arr:
            idx = num + 2
            while table[idx] == 3:
                idx += 1
            for i in range(idx, idx + depth):
                table[i] += 1
        for i in range(199, 0, -1):
            if table[i]:
                return i
    else:
        return 0


def solve(arr):
    global ans
    go_A = []
    go_B = []
    for i in range(len_p):
        if arr[i] == 0:
            go_A.append(dist[i][0])
        else:
            go_B.append(dist[i][1])
    go_A.sort()  # s1
    go_B.sort()  # s2
    ans = min(ans, max(solve2(go_A, 0), solve2(go_B, 1)))


def subset(arr, depth):
    if depth == len_p:
        solve(arr)
    else:
        for i in range(2):
            ar = arr[:]
            ar.append(i)
            subset(ar, depth + 1)


for T in range(1, int(input()) + 1):
    ans = 1e9
    N = int(input())
    people = []
    len_p = 0
    stairs = []
    for r in range(N):
        row = list(map(int, input().split()))
        for c in range(N):
            if row[c] == 1:
                people.append((r, c))
                len_p += 1
            elif row[c] > 1:
                stairs.append((r, c, row[c]))
    dist = [[abs(pr - sr) + abs(pc - sc) for sr, sc, _ in stairs] for pr, pc in people]
    subset([], 0)
    print('#{} {}'.format(T, ans))