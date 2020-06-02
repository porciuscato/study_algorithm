import sys

sys.stdin = open('4131.txt')


def isflat(array, start, end):
    if start < 0 or end >= N:
        return False
    for ii in range(start, end):
        if array[ii] != array[ii + 1]:
            return False
    return True


def solve(array):
    global answer
    all_same = True
    for idx in range(N - 1):
        value = abs(array[idx] - array[idx + 1])
        if value >= 2:
            return
        if value != 0:
            all_same = False
    if all_same:
        answer += 1
        return
    upslope = [False] * N
    downslope = [False] * N
    for idx in range(N - 1):
        if array[idx] + 1 == array[idx + 1]:
            s1 = idx - X + 1
            e1 = idx
            if isflat(array, s1, e1):
                for usi in range(s1, e1 + 1):
                    upslope[usi] = True
            else:
                return
        elif array[idx] - 1 == array[idx + 1]:
            s2 = idx + 1
            e2 = idx + X
            if isflat(array, s2, e2):
                for dsi in range(s2, e2 + 1):
                    downslope[dsi] = True
            else:
                return
    for iii in range(N):
        if upslope[iii] and downslope[iii]:
            return
    answer += 1


for T in range(1, int(input()) + 1):
    answer = 0
    N, X = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        solve(land[i])
    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(land[j][i])
        solve(temp)
    print("#{} {}".format(T, answer))
