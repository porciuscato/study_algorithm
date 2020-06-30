def fill_board(board, length, center):
    directions = ((0, 1), (-1, 0), (0, -1), (1, 0))
    direc = 0
    limit = length ** 2
    row, col = center, center
    for i in range(2, limit + 1):
        dr, dc = directions[direc]
        nr, nc = row + dr, col + dc
        if 0 <= nr < limit and 0 <= nc < limit and not board[nr][nc]:
            board[nr][nc] = i
        else:
            direc = (direc - 1) % 4
            dr, dc = directions[direc]
            nr, nc = row + dr, col + dc
            board[nr][nc] = i
        direc = (direc + 1) % 4
        row = nr
        col = nc


def print_answer(arr, board):
    r1, c1, r2, c2 = arr
    mx = 0
    for j in range(c1, c2 + 1):
        mx = max((mx, board[r1][j], board[r2][j]))
    length = len(str(mx))
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            print(str(board[i][j]).rjust(length, " "), end=" ")
        print()


def main():
    # origin = list(map(int, input().split()))

    from time import time
    st = time()
    origin = [-4, -4, 2, 0]
    mx = max(list(map(abs, origin)))
    length = 2 * mx + 1
    board = [[0 for _ in range(length)] for __ in range(length)]
    board[mx][mx] = 1
    origin = list(map(lambda x: x + mx, origin))
    fill_board(board, length, mx)
    print_answer(origin, board)
    print(time() - st)


main()


# -5000 -5000 -4951 -4996

# -4000 -4000 -3951 -4000
# [-5000, -3000, -4951, -2997]
# [-4, -4, 5, 0]