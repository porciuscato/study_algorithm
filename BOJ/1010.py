def main():
    board = [[0 for _ in range(31)] for __ in range(31)]
    for i in range(31):
        board[0][i] = 1
    for i in range(1, 31):
        for j in range(i, 31):
            board[i][j] = board[i][j - 1] + board[i - 1][j - 1]
    for _ in range(int(input())):
        N, M = map(int, input().split())
        print(board[N][M])
        pass


main()
