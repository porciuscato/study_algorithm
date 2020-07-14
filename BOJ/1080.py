def main():
    N, M = map(int, input().split())
    board = [list(map(int, list(input()))) for _ in range(N)]
    origin = [list(map(int, list(input()))) for _ in range(N)]
    ans = 0
    for row in range(N - 2):
        for col in range(M - 2):
            if board[row][col] != origin[row][col]:
                ans += 1
                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        board[r][c] = 1 - board[r][c]
    for row in range(N):
        for col in range(M):
            if board[row][col] != origin[row][col]:
                ans = -1
    return ans


if __name__ == '__main__':
    print(main())
