import sys

sys.stdin = open('input.txt', 'r')

delta = ((-1, 0), (0, 1), (1, 0), (0, -1))


def bfs(row, col):
    global ans, G, vis
    que = []
    tot = 0
    que.append((row, col))
    vis[row][col] = 1
    tot += G[row][col]
    front = -1
    rear = 0
    while front != rear:
        front += 1
        tr, tc = que[front]
        for d in delta:
            dr = tr + d[0]
            dc = tc + d[1]
            if 0 <= dr < N and 0 <= dc < N and not vis[dr][dc] and L <= abs(G[tr][tc] - G[dr][dc]) <= R:
                vis[dr][dc] = 1
                que.append((dr, dc))
                rear += 1
                tot += G[dr][dc]
    result = int(tot / len(que))
    for row, col in que:
        G[row][col] = result


N, L, R = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
ans = 0
while True:
    check = False
    vis = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            for d in delta:
                dr = r + d[0]
                dc = c + d[1]
                if 0 <= dr < N and 0 <= dc < N and not vis[r][c] and L <= abs(G[r][c] - G[dr][dc]) <= R:
                    bfs(r, c)
                    check = True
                    break
    if check:
        ans += 1
    else:
        break

print(ans)
