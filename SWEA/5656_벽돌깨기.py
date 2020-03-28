import sys

sys.stdin = open('5656.txt', 'r')


def clear(copied_board):
    board = [[0 for _ in range(W)] for __ in range(H)]
    for h in range(H):
        for w in range(W):
            board[h][w] = copied_board[h][w]

    for w in range(W):
        numbers = []
        for h in range(H - 1, -1, -1):
            if board[h][w]:
                numbers.append(board[h][w])
                board[h][w] = 0
        for i in range(len(numbers)):
            board[H - 1 - i][w] = numbers[i]
    return board


def remove(x, y, copied_board):
    board = [[0 for _ in range(W)] for __ in range(H)]
    for h in range(H):
        for w in range(W):
            board[h][w] = copied_board[h][w]
    delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
    # 이것만 깨면 된다.
    bricks = []
    return board


def solve(x, y, copied_board, n):
    global H, W, ANSWER
    if n == N:
        count = 0
        for h in range(H):
            for w in range(W):
                if copied_board[h][w]:
                    count += 1
        ANSWER = min(ANSWER, count)
    else:
        board = [[0 for _ in range(W)] for __ in range(H)]
        for h in range(H):
            for w in range(W):
                board[h][w] = copied_board[h][w]
        board = remove(x, y, board)
        board = clear(board)

        for h in range(H):
            for w in range(W):
                if board[h][w]:
                    solve(h, w, board, n + 1)


for T in range(1, int(input()) + 1):
    N, W, H = map(int, input().split())
    ANSWER = 1e+6
    BOARD = [list(map(int, input().split())) for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if BOARD[h][w]:
                print(h, w)
                solve(h, w, BOARD, 0)
    print('#{} {}'.format(T, ANSWER))