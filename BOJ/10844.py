def main():
    N = int(input())
    div = 1000000000
    board = [[0 for _ in range(10)] for __ in range(N + 1)]
    for i in range(1, 10):
        board[1][i] = 1
    row = 2
    while row <= N:
        for i in range(10):
            if i == 0:
                board[row][i] = board[row - 1][i + 1] % div
            elif i == 9:
                board[row][i] = board[row - 1][i - 1] % div
            else:
                board[row][i] = (board[row - 1][i - 1] + board[row - 1][i + 1]) % div
        row += 1
    print(sum(board[N]) % div)


main()
