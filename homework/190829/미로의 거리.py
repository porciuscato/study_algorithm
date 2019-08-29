dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for T in range(1, int(input()) + 1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    start = 0
    x = y = 0
    while x < N:
        if maze[x][y] == 2:
            start = [x, y]
            break
        y += 1
        if y == N:
            x += 1
            y = 0


    def isvalid(x, y):
        if (0 <= x < N and 0 <= y < N) and (maze[x][y] == 0 or maze[x][y] == 3):
            return True
        else:
            return False


    que = []
    que.append([start, 0])
    visited[x][y] = 1
    flag = 0
    while que:
        temp = que.pop(0)
        if maze[temp[0][0]][temp[0][1]] == 3:
            flag = temp[1] - 1
            break
        for i in range(4):
            nx = temp[0][0] + dx[i]
            ny = temp[0][1] + dy[i]
            if isvalid(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = 1
                depth = temp[1] + 1
                que.append([[nx, ny], depth])

    print('#{} {}'.format(T, flag))
