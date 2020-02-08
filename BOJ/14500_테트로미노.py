import sys

sys.stdin = open("14500.txt")

TETROMINO = (
    ((0, 1), (0, 2), (0, 3)),
    ((1, 0), (2, 0), (3, 0)),

    ((0, 1), (1, 0), (1, 1)),

    ((1, 0), (2, 0), (2, 1)),
    ((0, 1), (0, 2), (1, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 1), (0, 2), (-1, 2)),
    ((0, 1), (-1, 1), (-2, 1)),
    ((1, 0), (1, 1), (1, 2)),
    ((0, 1), (1, 0), (2, 0)),
    ((0, 1), (0, 2), (1, 2)),

    ((1, 0), (1, 1), (2, 1)),
    ((0, 1), (-1, 1), (-1, 2)),
    ((0, 1), (-1, 1), (1, 0)),
    ((0, 1), (1, 1), (1, 2)),

    ((0, 1), (0, 2), (1, 1)),
    ((0, 1), (-1, 1), (1, 1)),
    ((0, 1), (-1, 1), (0, 2)),
    ((1, 0), (1, 1), (2, 0)),
)


def is_valid(TET, row, col):
    global SERO, KARO
    for te_r, te_c in TET:
        if 0 <= row + te_r < SERO and 0 <= col + te_c < KARO:
            continue
        else:
            return False
    return True


def calculate(TET, row, col):
    global ANSWER
    total = TABLE[row][col]
    for te_r, te_c in TET:
        total += TABLE[row + te_r][col + te_c]
    ANSWER = max(ANSWER, total)


if __name__ == '__main__':
    SERO, KARO = map(int, input().split())
    TABLE = [list(map(int, input().split())) for _ in range(SERO)]
    ANSWER = 0
    for row in range(SERO):
        for col in range(KARO):
            for TET in TETROMINO:
                if is_valid(TET, row, col):
                    calculate(TET, row, col)
    print(ANSWER)