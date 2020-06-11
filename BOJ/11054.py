import sys

sys.stdin = open("11054.txt")


def increase(board, N):
    for i in range(N):
        val = board[0][i]
        temp = []
        for j in range(i - 1, -1, -1):
            if val > board[0][j]:
                temp.append(board[1][j])
        try:
            board[1][i] = max(temp) + 1
        except ValueError:
            pass


def decrease(board, N):
    for i in range(N - 1, -1, -1):
        val = board[0][i]
        temp = []
        for j in range(i + 1, N):
            if val > board[0][j]:
                temp.append(board[2][j])
        try:
            board[2][i] = max(temp) + 1
        except ValueError:
            continue


def solve(board, N):
    answer = 0
    for n in range(N):
        board[3][n] = board[1][n] + board[2][n] - 1
        answer = max(answer, board[3][n])
    return answer


def main():
    N = int(input())
    board = [list(map(int, input().split()))]
    for _ in range(3):
        board.extend([[1 for __ in range(N)]])
    increase(board, N)
    decrease(board, N)
    return solve(board, N)


print(main())
