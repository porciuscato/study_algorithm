for T in range(1, int(input()) + 1):
    board = [[0 for i in range(10)] for i in range(10)]
    N = int(input())
    count = 0
    for n in range(N):
        r1, c1, r2, c2, color = list(map(int, input().split()))
        for x in range(r1, r2 + 1):
            for y in range(c1, c2 + 1):
                target = board[x][y]
                if color == 1:
                    if target == 0:
                        board[x][y] = 1
                    elif target == 2:
                        board[x][y] = 3
                        count += 1
                elif color == 2:
                    if target == 0:
                        board[x][y] = 2
                    elif target == 1:
                        board[x][y] = 3
                        count += 1
    print('#{} {}'.format(T, count))