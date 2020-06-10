import sys

sys.stdin = open("2580.txt")


class Blank:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.possibles = []
        self.area = ()


def area_check(r, c):
    checkpoints = [0, 3, 6, 9]
    for i in range(3):
        if checkpoints[i] <= r < checkpoints[i + 1]:
            area_row = (checkpoints[i], checkpoints[i + 1])
        if checkpoints[i] <= c < checkpoints[i + 1]:
            area_col = (checkpoints[i], checkpoints[i + 1])
    return area_row, area_col


def find_possibles(board, blank):
    r = blank.row
    c = blank.col
    visited = [False] * 10
    # 가로
    for i in range(9):
        val = board[r][i]
        if not visited[val]:
            visited[val] = True
    # 세로
    for j in range(9):
        val = board[j][c]
        if not visited[val]:
            visited[val] = True
    # 영역
    area_range = blank.area
    for i in range(area_range[0][0], area_range[0][1]):
        for j in range(area_range[1][0], area_range[1][1]):
            val = board[i][j]
            if not visited[val]:
                visited[val] = True
    # 처리
    result = [v for v in range(1, 10) if not visited[v]]
    return result


def collect_blanks(board: list) -> list:
    result = []
    for r in range(9):
        for c in range(9):
            if not board[r][c]:
                blank = Blank(r, c)
                blank.area = area_check(r, c)
                blank.possibles = find_possibles(board, blank)
                result.append(blank)
    return result


def print_board(board):
    for r in range(9):
        for c in range(9):
            print(board[r][c], end=" ")
        print()


def isvalid(board, blank, possible):
    r = blank.row
    c = blank.col
    board[r][c] = possible
    # 가로
    visited = [0] * 10
    for i in range(9):
        visited[board[r][i]] += 1
    for v in range(1, 10):
        if visited[v] > 1:
            board[r][c] = 0
            return False
    # 세로
    visited = [0] * 10
    for j in range(9):
        visited[board[j][c]] += 1
    for v in range(1, 10):
        if visited[v] > 1:
            board[r][c] = 0
            return False
    # 영역
    visited = [0] * 10
    area_range = blank.area
    for i in range(area_range[0][0], area_range[0][1]):
        for j in range(area_range[1][0], area_range[1][1]):
            visited[board[i][j]] += 1
    for v in range(1, 10):
        if visited[v] > 1:
            board[r][c] = 0
            return False
    return True


def recursive(board, blanks, depth, length):
    if depth == length:
        print_board(board)
        return True
    else:
        blank = blanks[depth]
        possibles = blank.possibles
        for possible in possibles:
            if isvalid(board, blank, possible):
                result = recursive(board, blanks, depth + 1, length)
                if result:
                    return True
                else:
                    board[blank.row][blank.col] = 0


def solve(board, blanks):
    recursive(board, blanks, 0, len(blanks))


def main():
    board = [list(map(int, input().split())) for _ in range(9)]
    blanks = collect_blanks(board)
    solve(board, blanks)


main()
