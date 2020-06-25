def main():
    n, k = map(int, input().split())
    weights = [0] * (n + 1)
    values = [0] * (n + 1)
    for i in range(1, n + 1):
        weights[i], values[i] = map(int, input().split())
    board = [[0 for _ in range(100001)] for __ in range(n + 1)]
    for row in range(1, n + 1):
        for col in range(1, k + 1):
            board[row][col] = board[row - 1][col]
            if col - weights[row] >= 0:
                board[row][col] = max(board[row][col], board[row][col - weights[row]] + values[row])
    print(board[n][k])


main()
