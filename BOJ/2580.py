import sys

sys.stdin = open("2580.txt")


class Blank:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.possibles = []

    def __repr__(self):
        return "({}, {}, {})".format(self.row, self.col, self.possibles)


def area_check(r, c):
    checkpoints = [0, 3, 6, 9]
    for i in range(3):
        if checkpoints[i] <= r < checkpoints[i + 1]:
            area_row = (checkpoints[i], checkpoints[i + 1])
        if checkpoints[i] <= c < checkpoints[i + 1]:
            area_col = (checkpoints[i], checkpoints[i + 1])
    return area_row, area_col


def find_possibles(board, r, c):
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
    area_range = area_check(r, c)
    for i in range(area_range[0][0], area_range[0][1]):
        for j in range(area_range[1][0], area_range[1][1]):
            val = board[i][j]
            if not visited[val]:
                visited[val] = True
    # 처리
    result = [v for v in range(1, 10) if not visited[v]]
    return result


def collect_blanks(board) -> list:
    result = []
    for r in range(9):
        for c in range(9):
            if not board[r][c]:
                blank = Blank(r, c)
                blank.possibles = find_possibles(board, r, c)
                result.append(blank)
    return result


def print_board(board):
    for r in range(9):
        for c in range(9):
            print(board[r][c], end=" ")
        print()


def solve(board, blanks):
    # 여기서 재귀 함수를 호출하여
    pass


def main():
    board = [list(map(int, input().split())) for _ in range(9)]
    # 가능한 후보들을 possibles에 정리
    blanks = collect_blanks(board)
    # 하나씩 선택해서 재귀 함수로 구현
    solve(board, blanks)
    # 정답 출력
    print_board(board)


main()
