import sys

input = sys.stdin.readline


def turn_90d(row, col, length, direc):
    temp = [[0 for _ in range(12)] for __ in range(12)]
    for r in range(length):
        for c in range(length):
            if direc:
                temp[row + c][col + length - 1 - r] = cube[row + r][col + c]
            else:
                temp[row + length - 1 - c][col + r] = cube[row + r][col + c]
    for r in range(row, row + length):
        for c in range(col, col + length):
            cube[r][c] = temp[r][c]


def turn_180d(row, col, length):
    temp = [[0 for _ in range(12)] for __ in range(12)]
    for r in range(length):
        for c in range(length):
            temp[row + length - 1 - r][col + length - 1 - c] = cube[row + r][col + c]
    for r in range(row, row + length):
        for c in range(col, col + length):
            cube[r][c] = temp[r][c]


def up_once():
    for c in range(3, 6):
        temp = []
        for r in range(3, 15):
            temp.append(cube[r % 12][c])
        for r in range(12):
            cube[r][c] = temp[r]
    turn_90d(3, 6, 3, 1)
    turn_90d(3, 0, 3, 0)


def up_twice():
    for c in range(3, 6):
        temp = []
        for r in range(6, 18):
            temp.append(cube[r % 12][c])
        for r in range(12):
            cube[r][c] = temp[r]
    turn_180d(3, 6, 3)
    turn_180d(3, 0, 3)


def turn_half():
    turn_180d(0, 0, 9)
    turn_180d(9, 3, 3)


def turn_right():
    turn_90d(0, 0, 9, 1)
    turn_90d(9, 3, 3, 0)


def turn_left():
    turn_90d(0, 0, 9, 0)
    turn_90d(9, 3, 3, 1)


def view(dimen):
    if dimen == 'F':
        up_once()
    elif dimen == 'B':
        turn_half()
        up_once()
    elif dimen == 'R':
        turn_right()
        up_once()
    elif dimen == 'L':
        turn_left()
        up_once()
    elif dimen == 'D':
        up_twice()


def rotate(direc):
    if direc == '+':
        turn_90d(2, 2, 5, 1)
    else:
        turn_90d(2, 2, 5, 0)


def down_once():
    for c in range(3, 6):
        temp = []
        for r in range(9, 21):
            temp.append(cube[r % 12][c])
        for r in range(12):
            cube[r][c] = temp[r]
    turn_90d(3, 6, 3, 0)
    turn_90d(3, 0, 3, 1)


def restore(dimen):
    if dimen == 'F':
        down_once()
    elif dimen == 'B':
        turn_half()
        up_once()
    elif dimen == 'R':
        down_once()
        turn_90d(0, 0, 9, 0)
        turn_90d(9, 3, 3, 1)
    elif dimen == 'L':
        down_once()
        turn_90d(0, 0, 9, 1)
        turn_90d(9, 3, 3, 0)
    elif dimen == 'D':
        up_twice()


def cube_print():
    for i in range(3, 6):
        print(''.join(cube[i][3:6]))


if __name__ == "__main__":
    for _ in range(int(input())):
        n = input()
        operations = input()[:-1].split()
        cube = [
            ['-', '-', '-', 'o', 'o', 'o', '-', '-', '-'],
            ['-', '-', '-', 'o', 'o', 'o', '-', '-', '-'],
            ['-', '-', '-', 'o', 'o', 'o', '-', '-', '-'],
            ['g', 'g', 'g', 'w', 'w', 'w', 'b', 'b', 'b'],
            ['g', 'g', 'g', 'w', 'w', 'w', 'b', 'b', 'b'],
            ['g', 'g', 'g', 'w', 'w', 'w', 'b', 'b', 'b'],
            ['-', '-', '-', 'r', 'r', 'r', '-', '-', '-'],
            ['-', '-', '-', 'r', 'r', 'r', '-', '-', '-'],
            ['-', '-', '-', 'r', 'r', 'r', '-', '-', '-'],
            ['-', '-', '-', 'y', 'y', 'y', '-', '-', '-'],
            ['-', '-', '-', 'y', 'y', 'y', '-', '-', '-'],
            ['-', '-', '-', 'y', 'y', 'y', '-', '-', '-']
        ]
        for oper in operations:
            view(oper[0])
            rotate(oper[1])
            restore(oper[0])
        cube_print()

# 1
# 16
# U+ R+ R+ F+ F+ R+ R+ U+ F+ F+ R+ R+ F+ F+ U- L+
