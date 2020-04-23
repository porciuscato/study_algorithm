import sys

sys.stdin = open('1227.txt', 'r')

SIZE = 100

for T in range(10):
    answer = 0
    t = input()
    MAZE = [list(map(int, list(input()))) for _ in range(100)]
    start = ()
    for i in range(SIZE):
        for j in range(SIZE):
            if MAZE[i][j] == 2:
                start = (i, j)
                break
    que = [start]
    visited = [[0] * SIZE for _ in range(SIZE)]
    visited[start[0]][start[1]] = 1
    while que:
        x, y = que.pop(0)
        if MAZE[x][y] == 3:
            answer = 1
            break
        else:
            for dtx, dty in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                dx = x + dtx
                dy = y + dty
                if MAZE[dx][dy] in (0, 3) and not visited[dx][dy]:
                    que.append((dx, dy))
                    visited[dx][dy] = 1
    print(f'#{t} {answer}')
