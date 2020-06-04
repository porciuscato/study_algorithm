import sys

sys.stdin = open("5656.txt", "r")


from collections import deque


def crush(array, column):
    visited = [[False for _ in range(W)] for __ in range(H)]
    for now in range(H):
        if array[now][column]:
            break
    else:
        return False
    que = deque([])
    que.append((now, column))
    visited[now][column] = True
    while que:
        n_r, n_c = que.popleft()
        size = array[n_r][n_c]
        array[n_r][n_c] = 0
        for de in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            p_r, p_c = n_r, n_c
            for i in range(1, size):
                p_r += de[0]
                p_c += de[1]
                if 0 <= p_r < H and 0 <= p_c < W and not visited[p_r][p_c] and array[p_r][p_c]:
                    que.append((p_r, p_c))
                    visited[p_r][p_c] = True
    return True


def down(array):
    for w in range(W):
        now = H - 1
        pos = H - 1
        while now >= 0 and pos >= 0:
            if array[now][w] == 0:
                pos = now - 1
                while pos >= 0 and array[pos][w] == 0:
                    pos -= 1
                if pos < 0:
                    break
                if array[pos][w]:
                    array[pos][w], array[now][w] = array[now][w], array[pos][w]
                    now -= 1
            else:
                now -= 1


def solve(arr):
    global answer
    if answer == 0:
        return
    copied = []
    for r in range(H):
        temp = []
        for c in range(W):
            temp.append(board[r][c])
        copied.append(temp)

    for chosen in arr:
        crush(copied, chosen)
        down(copied)
    ans = 0
    for i1 in range(H):
        for j1 in range(W):
            if copied[i1][j1]:
                ans += 1
    answer = min(answer, ans)


def permu_with(origin, aim, depth, arr, size):
    if depth == aim:
        solve(arr)
    else:
        for idx in range(size):
            ar = arr[:]
            ar.append(origin[idx])
            permu_with(origin, aim, depth + 1, ar, size)


for T in range(1, int(input()) + 1):
    N, W, H = map(int, input().split())
    selection = [i for i in range(W)]
    board = []
    answer = 0
    for row in range(H):
        temp = list(map(int, input().split()))
        for t in temp:
            if t:
                answer += 1
        board.append(temp)
    permu_with(selection, N, 0, [], W)
    print("#{} {}".format(T, answer))

