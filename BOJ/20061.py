def find_possible_pos(pos, direc) -> int:
    row = 0
    col = 0
    if direc == "r":
        row = pos
    else:
        col = pos
    for i in range(6, SIZE):
        if direc == "r":
            if board[row][i]:
                return i - 1
        else:
            if board[i][col]:
                return i - 1
    return SIZE - 1


def set_board(block, row, col) -> None:
    global board
    if block == 1:
        right_col = find_possible_pos(row, "r")
        board[row][right_col] = 1

        bottom_row = find_possible_pos(col, "b")
        board[bottom_row][col] = 1
    elif block == 2:
        right_col = find_possible_pos(row, 'r')
        board[row][right_col] = 2
        board[row][right_col - 1] = 2

        bottom_row = min(find_possible_pos(col, 'b'), find_possible_pos(col + 1, 'b'))
        board[bottom_row][col] = 2
        board[bottom_row][col + 1] = 2
    else:
        right_col = min(find_possible_pos(row, 'r'), find_possible_pos(row + 1, 'r'))
        board[row][right_col] = 3
        board[row + 1][right_col] = 3

        bottom_row = find_possible_pos(col, 'b')
        board[bottom_row - 1][col] = 3
        board[bottom_row][col] = 3


def move(pos, num, direc) -> None:
    global board
    row = pos
    col = pos
    end = 4 if num == 1 else 5
    if direc == 'r':
        for r in range(4):
            for c in range(col, end, -1):
                board[r][c] = board[r][c - num]
    else:
        for c in range(4):
            for r in range(row, end, -1):
                board[r][c] = board[r - num][c]

    for i in range(4):
        if direc == 'r':
            board[i][4] = 0
            if num == 2:
                board[i][5] = 0
        else:
            board[4][i] = 0
            if num == 2:
                board[5][i] = 0


def score_check(direc) -> None:
    global answer
    start = 9
    while start >= 4:
        if direc == 'r':
            for r in range(4):
                if board[r][start] == 0:
                    start -= 1
                    break
            else:
                answer += 1
                move(start, 1, 'r')
        else:
            for c in range(4):
                if board[start][c] == 0:
                    start -= 1
                    break
            else:
                answer += 1
                move(start, 1, 'b')


def timid_check(direc) -> int:
    if direc == 'r':
        for c in range(4, 6):
            for r in range(4):
                if board[r][c]:
                    return 6 - c
    else:
        for r in range(4, 6):
            for c in range(4):
                if board[r][c]:
                    return 6 - r
    return 0


def main() -> None:
    for _ in range(int(input())):
        block, r, c = map(int, input().split())
        set_board(block, r, c)
        score_check('r')
        score_check('b')
        right_move = timid_check('r')
        bottom_move = timid_check('b')
        if right_move:
            move(9, right_move, 'r')
        if bottom_move:
            move(9, bottom_move, 'b')


if __name__ == "__main__":
    SIZE = 10
    board = [[0 for _ in range(SIZE)] for __ in range(SIZE)]
    answer = 0
    remain = 0
    main()
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] > 0:
                remain += 1
    print(f'{answer}\n{remain}\n')

