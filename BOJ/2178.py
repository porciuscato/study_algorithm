import sys

sys.stdin = open('input.txt', 'r')

delta = ((-1, 0), (0, 1), (1, 0), (0, -1))


def bfs(r, c):
    global ans, v
    q = []
    front = rear = -1
    q.append((r, c, 1))
    v[r][c] = 1
    rear += 1
    while front != rear:
        front += 1
        tr, tc, dis = q[front]
        for d in delta:
            dr = tr + d[0]
            dc = tc + d[1]
            if 0 <= dr < N and 0 <= dc < M and not v[dr][dc] and data[dr][dc]:
                if dr == N - 1 and dc == M - 1:
                    ans = dis + 1
                    return
                q.append((dr, dc, dis + 1))
                rear += 1
                v[dr][dc] = 1


N, M = map(int, input().split())
data = [list(map(int, list(input()))) for _ in range(N)]
v = [[0] * M for _ in range(N)]
ans = 0
bfs(0, 0)
print(ans)
