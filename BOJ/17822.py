import sys
from collections import deque

input = sys.stdin.readline


def rotate(rem, direc, ite):
    for i in range(1, N + 1):
        if i % rem == 0:
            for _ in range(ite):
                if direc == 0:
                    board[i].rotate(1)
                else:
                    board[i].rotate(-1)


def del_adjacent():
    flag = False
    visited = [[False for _ in range(M)] for __ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(M):
            if board[i][j] > 0 and not visited[i][j]:
                pos = False
                value = board[i][j]
                que = [(i, j)]
                front = -1
                rear = 0
                visited[i][j] = True
                while front != rear:
                    front += 1
                    row, col = que[front]
                    for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                        nr = row + dr
                        nc = (col + dc) % M
                        if 1 <= nr <= N and board[nr][nc] > 0:
                            if not visited[nr][nc] and board[nr][nc] == value:
                                que.append((nr, nc))
                                visited[nr][nc] = True
                                rear += 1
                                pos = True
                                flag = True
                if pos:
                    for r, c in que:
                        board[r][c] = 0
    return True if flag else False


def print_result():
    result = 0
    for i in range(1, N + 1):
        result += sum(board[i])
    print(result)


def make_average():
    cnt = 0
    tot = 0
    cors = []
    for i in range(1, N + 1):
        for j in range(M):
            if board[i][j]:
                cnt += 1
                tot += board[i][j]
                cors.append((i, j))
    if cnt > 0:
        avg = tot / cnt
        for r, c in cors:
            if board[r][c] > avg:
                board[r][c] -= 1
            elif board[r][c] < avg:
                board[r][c] += 1


if __name__ == "__main__":
    N, M, T = map(int, input().split())
    board = [deque([])]
    for _ in range(N):
        board.append(deque(list(map(int, input().split()))))
    for _ in range(T):
        x, d, k = map(int, input().split())
        rotate(x, d, k)
        if not del_adjacent():
            make_average()
    print_result()

