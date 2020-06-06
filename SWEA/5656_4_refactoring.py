import sys

sys.stdin = open("5656.txt", "r")


from collections import deque


def bomb(column):
    visited = [[False for _ in range(W)] for __ in range(H)]
    for now in range(H):
        if Data[now][column]:
            break
    else:
        return
    que = deque([])
    que.append((now, column))
    visited[now][column] = True
    while que:
        n_r, n_c = que.popleft()
        size = Data[n_r][n_c]
        Data[n_r][n_c] = 0
        for de in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            p_r, p_c = n_r, n_c
            for i in range(1, size):
                p_r += de[0]
                p_c += de[1]
                if 0 <= p_r < H and 0 <= p_c < W and not visited[p_r][p_c] and Data[p_r][p_c]:
                    que.append((p_r, p_c))
                    visited[p_r][p_c] = True


def block_check():
    global answer
    temp = 0
    for h in range(H):
        for w in range(W):
            if Data[h][w]:
                temp += 1
    answer = min(answer, temp)


def down():
    for w in range(W):
        now = H - 1
        pos = H - 1
        while now >= 0 and pos >= 0:
            if Data[now][w] == 0:
                pos = now - 1
                while pos >= 0 and Data[pos][w] == 0:
                    pos -= 1
                if pos < 0:
                    break
                if Data[pos][w]:
                    Data[pos][w], Data[now][w] = Data[now][w], Data[pos][w]
                    now -= 1
            else:
                now -= 1


def data_init():
    for h in range(H):
        for w in range(W):
            Data[h][w] = Origin[h][w]


def solve(arr):
    if answer == 0:
        return
    data_init()
    for ele in arr:
        bomb(ele)
        down()
    block_check()


def permu(arr, depth):
    if depth == N:
        solve(arr)
    else:
        for w in range(W):
            ar = arr[:]
            ar.append(w)
            permu(ar, depth + 1)


for T in range(1, int(input()) + 1):
    answer = 0
    N, W, H = map(int, input().split())
    Origin = [list(map(int, input().split())) for _ in range(H)]
    Data = [[Origin[__][_] for _ in range(W)] for __ in range(H)]
    answer = 1e9
    permu([], 0)
    print("#{} {}".format(T, answer))