import sys

sys.stdin = open('input.txt', 'r')

for T in range(1, int(input()) + 1):
    N = int(input())
    pan = [list(map(int, input().split())) for _ in range(N)]
    board = [[5] * (N + 2) for _ in range(N + 2)]
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            board[x][y] = pan[x - 1][y - 1]
    maxi = 0
    delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    direc = [0, 1, 2, 3]


    def isvalid(x, y):
        global maxi
        value = board[x][y]
        if value == -1:
            return False
        elif value == 5:
            maxi = 1
            return False
        else:
            return True

    def proceed(coordinate, direction):
        cx, cy = coordinate

        pass


    def chulbal(x, y):
        global maxi
        que = []
        for i in range(4):
            dx = x + delta[i][0]
            dy = y + delta[i][1]
            direc = i
            if isvalid(dx, dy):
                que.append([[dx, dy], direc])
        while que:
            coordinate, direction = que.pop(0)
            total = proceed(coordinate, direction)
            if maxi < total:
                maxi = total


    for x in range(N):
        for y in range(N):
            if pan[x][y] == 0:
                chulbal(x, y)

    print('#{} {}'.format(T, maxi))
