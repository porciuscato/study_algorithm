import sys

sys.stdin = open('lunchtime.txt', 'r')


def solve2(arr, inj):
    stair_depth = stairs[inj][2]
    if len(arr):
        length = len(arr)
        for i in range(length):
            arr[i] += 1
        idx = 0
        count = 0
        time = arr[0]
        result = []
        while time < ans:
            for i in range(idx, length):
                pass

            if idx == length:
                break
            time += 1
        try:
            return result[-1]
        except:
            return 1e5
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
    resultA = solve2(go_A, 0)
    resultB = solve2(go_B, 1)
    val = max(resultA, resultB)
    if val < ans:
        ans = val


def combi(arr, depth):
    if depth == len_p:
        solve(arr)
    else:
        ar = arr[:]
        ar.append(0)
        combi(ar, depth + 1)
        ar = arr[:]
        ar.append(1)
        combi(ar, depth + 1)


for T in range(1, int(input()) + 1):
    ans = 1e9
    N = int(input())
    people = []
    stairs = []
    for r in range(N):
        row = list(map(int, input().split()))
        for c in range(N):
            if row[c] == 1:
                people.append((r, c))
            elif row[c] > 1:
                stairs.append((r, c, row[c]))
    dist = [[abs(pr - sr) + abs(pc - sc) for sr, sc, _ in stairs] for pr, pc in people]
    len_p = len(people)
    combi([], 0)
    print('#{} {}'.format(T, ans))
