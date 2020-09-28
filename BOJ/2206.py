import sys
from collections import deque

input = sys.stdin.readline
MAX_VALUE = 10 ** 6


def bfs():
    global answer
    que = deque([(0, 0, 1, False)])
    while que:
        row, col, distance, broken = que.popleft()
        if row == ROW - 1 and col == COL - 1:
            answer = distance
            break
        for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            nr = row + dr
            nc = col + dc
            if 0 <= nr < ROW and 0 <= nc < COL:
                if not visited[nr][nc][0] or not visited[nr][nc][1]:
                    if BOARD[nr][nc]:
                        if not broken:
                            visited[nr][nc][1] = True
                            que.append((nr, nc, distance + 1, True))
                    else:
                        if not broken:
                            visited[nr][nc][0] = True
                            que.append((nr, nc, distance + 1, broken))
                        else:
                            if not visited[nr][nc][1]:
                                visited[nr][nc][1] = True
                                que.append((nr, nc, distance + 1, broken))


if __name__ == "__main__":
    ROW, COL = map(int, input().split())
    BOARD = [list(map(int, list(input()[:-1]))) for _ in range(ROW)]
    visited = [[[False, False] for _ in range(COL)] for __ in range(ROW)]
    visited[0][0][0] = True
    visited[0][0][1] = True
    answer = MAX_VALUE
    bfs()
    print(answer if answer != MAX_VALUE else -1)


# 3 6
# 011000
# 011010
# 100010

# 6 4
# 0100
# 1110
# 1000
# 0000
# 0111
# 0000

# 6 4
# 0000
# 1110
# 1000
# 0000
# 0111
# 0000
