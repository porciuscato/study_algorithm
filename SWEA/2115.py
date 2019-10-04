import sys

sys.stdin = open('input.txt', 'r')


def subset(row, cols, depth, tot, charr):
    global mx
    if depth == M:
        to = 0
        for j in range(len(charr)):
            to += sqr_B[r][charr[j]]
        if to > mx:
            mx = to
    else:
        t = tot + B[r][cols[depth]]
        ch = charr[:]
        if t <= C:
            ch.append(cols[depth])
            subset(row, cols, depth + 1, t, ch)
        subset(row, cols, depth + 1, tot, charr)


def isvalid(arr, candi):
    for ar in arr:
        if ar[0] != candi[0]:
            continue
        elif ar[1] & candi[1]:
            return False
        else:
            continue
    return True


def combi(arr, depth, last, hap):
    global ans
    if depth == 2:
        if hap > ans:
            ans = hap
    else:
        for k in range(last, pos_len):
            if isvalid(arr, pos[k]):
                ar = arr[:]
                ar.append(pos[k])
                combi(ar, depth + 1, k + 1, hap + pos[k][2])


for T in range(1, int(input()) + 1):
    N, M, C = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    sqr_B = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            sqr_B[r][c] = B[r][c] * B[r][c]
    ans = 0
    pos = []
    for r in range(N):
        for c in range(N - M + 1):
            arr = [r, [i for i in range(c, c + M)]]
            mx = 0
            subset(arr[0], arr[1], 0, 0, [])
            arr.append(mx)
            arr = [arr[0], set(arr[1]), arr[2]]
            pos.append(arr)
    pos_len = (N - M + 1) * N
    combi([], 0, 0, 0)
    print('#{} {}'.format(T, ans))
