import sys

input = sys.stdin.readline

if __name__ == "__main__":
    COL, ROW = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(ROW)]
    visited = [[False] * COL for _ in range(ROW)]
    ripes = []
    unripe = 0
    for i in range(ROW):
        for j in range(COL):
            if box[i][j] == 0:
                unripe += 1
            elif box[i][j] == 1:
                visited[i][j] = True
                ripes.append((i, j, 0))

    front = -1
    rear = len(ripes) - 1
    answer = 0
    while ripes and front != rear:
        front += 1
        row, col, time = ripes[front]
        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nr = row + dr
            nc = col + dc
            if 0 <= nr < ROW and 0 <= nc < COL:
                if not visited[nr][nc] and box[nr][nc] == 0:
                    visited[nr][nc] = True
                    ripes.append((nr, nc, time + 1))
                    rear += 1
                    unripe -= 1
                    answer = max(answer, time + 1)

    print(-1 if unripe else answer)




# 2 2
# 1 0
# 1 1

# 6 4
# 0 1 0 0 0 0
# 0 0 0 0 -1 -1
# 0 0 0 0 -1 0
# 0 0 0 0 -1 0

# 3 3
# 0 1 0
# -1 -1 -1
# 0 0 0

# 3 3
# 0 -1 0
# 1 -1 -1
# 0 0 0