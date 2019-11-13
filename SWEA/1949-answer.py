def dfs(x, y, h, usedk, pathl):
    global ans

    ans = max(ans, pathl)

    for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        xx, yy = x + dx, y + dy

        if not (0 <= xx < N and 0 <= yy < N): continue
        if visited[xx][yy]: continue

        visited[xx][yy] = 1

        if matNN[xx][yy] < h:
            dfs(xx, yy, matNN[xx][yy], usedk, pathl + 1)
        elif not usedk and matNN[xx][yy] - K < h:
            dfs(xx, yy, h - 1, 1, pathl + 1)

        visited[xx][yy] = 0


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    matNN = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    ans = 0

    highest = max(sum(matNN, []))

    for i in range(N):
        for j in range(N):
            if matNN[i][j] == highest:
                visited[i][j] = 1
                dfs(i, j, highest, 0, 1)
                visited[i][j] = 0

    print('#%d' % tc, ans)