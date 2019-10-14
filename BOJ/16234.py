import sys

sys.stdin = open('input.txt', 'r')

delta = ((-1, 0), (0, 1), (1, 0), (0, -1))


def dfs(row, col):
    global ans, G
    kingdom = []
    vis = [[0] * N for _ in range(N)]
    hap = 0
    stack = []
    f = r = -1
    stack.append((row, col))
    hap += G[row][col]
    vis[r][c] = 1
    while stack:
        tr, tc = stack.pop()
        for d in delta:
            dr = tr + d[0]
            dc = tc + d[1]
            if 0 <= dr < N and 0 <= dc < N and L <= abs(G[tr][tc] - G[dr][dc]) <= R:
                pass


N, L, R = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for r in range(N):
    for c in range(N):
        dfs(r, c)
