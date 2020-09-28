import sys

input = sys.stdin.readline


if __name__ == "__main__":
    COL, ROW, HEI = map(int, input().split())
    tomatoes = []
    for _ in range(HEI):
        tomatoes.append([list(map(int, input().split())) for _ in range(ROW)])
    visited = [[[False for _ in range(COL)] for __ in range(ROW)] for ___ in range(HEI)]
    ripes = []
    unripe = 0
    for h in range(HEI):
        for r in range(ROW):
            for c in range(COL):
                if tomatoes[h][r][c] == 0:
                    unripe += 1
                elif tomatoes[h][r][c] == 1:
                    visited[h][r][c] = True
                    ripes.append((h, r, c, 0))
    if unripe:
        answer = 0
        front = -1
        rear = len(ripes) - 1
        while front != rear:
            fin = False
            front += 1
            h, r, c, time = ripes[front]
            for dh, dr, dc in ((0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (-1, 0, 0), (1, 0, 0)):
                nh = h + dh
                nr = r + dr
                nc = c + dc
                if 0 <= nh < HEI and 0 <= nr < ROW and 0 <= nc < COL:
                    if tomatoes[nh][nr][nc] == 0 and not visited[nh][nr][nc]:
                        visited[nh][nr][nc] = True
                        unripe -= 1
                        ripes.append((nh, nr, nc, time + 1))
                        rear += 1
                        if unripe == 0:
                            answer = time + 1
                            fin = True
            if fin:
                break
        print(-1 if unripe else answer)
    else:
        print(0)
