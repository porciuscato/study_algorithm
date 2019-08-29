for T in range(1, int(input()) + 1):

    def isvalid(x, y):
        if 0 <= x < N and 0 <= y < N:
            return True
        else:
            return False


    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited = [[0] * N for _ in range(N)]
    stack = []
    result = 0

    for x in range(N):
        for y in range(N):
            if maze[x][y] == 2:
                visited[x][y] = 1
                stack.append([x, y])
                while stack:
                    cor = stack.pop(-1)
                    visited[cor[0]][cor[1]] = 1
                    for i in range(4):
                        cx = cor[0] + dx[i]
                        cy = cor[1] + dy[i]
                        if isvalid(cx, cy) and not visited[cx][cy]:
                            if maze[cx][cy] == 0:
                                stack.append([cx, cy])
                            elif maze[cx][cy] == 3:
                                result = 1
    print('#{} {}'.format(T, result))
