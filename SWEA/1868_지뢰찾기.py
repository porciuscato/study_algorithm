import sys

sys.stdin = open('1868.txt', 'r')

delta = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

for T in range(1, int(input()) + 1):
    answer = 0
    N = int(input())
    board = [list(input()) for _ in range(N)]
    # 전처리. * 주변은 '-'으로 바꾼다.
    for i in range(N):
        for j in range(N):
            if board[i][j] == '.':
                for dtx, dty in delta:
                    dx = i + dtx
                    dy = j + dty
                    if 0 <= dx < N and 0 <= dy < N and board[dx][dy] == '*':
                        board[i][j] = '-'
                        break
    # BFS 처리
    for ii in range(N):
        for jj in range(N):
            if board[ii][jj] == '.':
                answer += 1
                que = [(ii, jj)]
                board[ii][jj] = 0
                front = -1
                rear = 0
                while front != rear:
                    front += 1
                    x, y = que[front]
                    for dtx, dty in delta:
                        dx = x + dtx
                        dy = y + dty
                        if 0 <= dx < N and 0 <= dy < N:
                            if board[dx][dy] == '.':
                                board[dx][dy] = 0
                                que.append((dx, dy))
                                rear += 1
                            elif board[dx][dy] == '-':
                                board[dx][dy] = 0
    # '-' 처리
    for iii in range(N):
        for jjj in range(N):
            if board[iii][jjj] == '-':
                answer += 1
    print(f'#{T} {answer}')
