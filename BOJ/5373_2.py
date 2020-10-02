import sys

input = sys.stdin.readline

directions = ['U', 'F', 'D', 'B', 'L', 'R']
rotations = [
    ((3, 0), (5, 0), (1, 0), (4, 0)),
    ((0, 2), (5, 3), (2, 0), (4, 1)),
    ((1, 2), (5, 2), (3, 2), (4, 2)),
    ((0, 0), (4, 3), (2, 2), (5, 1)),
    ((0, 3), (1, 3), (2, 3), (3, 1)),
    ((0, 1), (3, 3), (2, 1), (1, 1)),
]
cube = [
    [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']],
    [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']],
    [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']],
    [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']],
    [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],
    [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]
]


def rotate_edges(front, direc):
    if front == 0:
        if direc == '+':
            cube[3][0][0], cube[3][0][1], cube[3][0][2], cube[5][0][0], cube[5][0][1], cube[5][0][2], cube[1][0][0], \
            cube[1][0][1], cube[1][0][2], cube[4][0][0], cube[4][0][1], cube[4][0][2], = cube[4][0][0], cube[4][0][1], \
                                                                                         cube[4][0][2], cube[3][0][0], \
                                                                                         cube[3][0][1], cube[3][0][2], \
                                                                                         cube[5][0][0], cube[5][0][1], \
                                                                                         cube[5][0][2], cube[1][0][0], \
                                                                                         cube[1][0][1], cube[1][0][2]
        else:
            cube[3][0][0], cube[3][0][1], cube[3][0][2], cube[3][0][0], cube[3][0][1], cube[3][0][2], cube[1][0][0], \
            cube[1][0][1], cube[1][0][2], cube[4][0][0], cube[4][0][1], cube[4][0][2], = cube[5][0][0], cube[5][0][1], \
                                                                                         cube[5][0][2], cube[1][0][0], \
                                                                                         cube[1][0][1], cube[1][0][2], \
                                                                                         cube[4][0][0], cube[4][0][1], \
                                                                                         cube[4][0][2], cube[3][0][0], \
                                                                                         cube[3][0][1], cube[3][0][2]
    elif front == 1:
        if direc == '+':
            cube[0][2][0], cube[0][2][1], cube[0][2][2], cube[5][0][0], cube[5][1][0], cube[5][2][0], cube[2][0][0], \
            cube[2][0][1], cube[2][0][2], cube[4][0][2], cube[4][1][2], cube[4][2][2] = cube[4][0][2], cube[4][1][2], \
                                                                                        cube[4][2][2], cube[0][2][0], \
                                                                                        cube[0][2][1], cube[0][2][2], \
                                                                                        cube[5][0][0], cube[5][1][0], \
                                                                                        cube[5][2][0], cube[2][0][0], \
                                                                                        cube[2][0][1], cube[2][0][2]
        else:
            cube[0][2][0], cube[0][2][1], cube[0][2][2], cube[5][0][0], cube[5][1][0], cube[5][2][0], cube[2][0][0], \
            cube[2][0][1], cube[2][0][2], cube[4][0][2], cube[4][1][2], cube[4][2][2] = cube[5][0][0], cube[5][1][0], \
                                                                                        cube[5][2][0], cube[2][0][0], \
                                                                                        cube[2][0][1], cube[2][0][2], \
                                                                                        cube[4][0][2], cube[4][1][2], \
                                                                                        cube[4][2][2], cube[0][2][0], \
                                                                                        cube[0][2][1], cube[0][2][2]
    elif front == 2:
        if direc == '+':
            cube[1][2][0], cube[1][2][1], cube[1][2][2], cube[5][2][0], cube[5][2][1], cube[5][2][2], cube[3][2][0], \
            cube[3][2][1], cube[3][2][2], cube[4][2][0], cube[4][2][1], cube[4][2][2] = cube[4][2][0], cube[4][2][1], \
                                                                                        cube[4][2][2], cube[1][2][0], \
                                                                                        cube[1][2][1], cube[1][2][2], \
                                                                                        cube[5][2][0], cube[5][2][1], \
                                                                                        cube[5][2][2], cube[3][2][0], \
                                                                                        cube[3][2][1], cube[3][2][2]
        else:
            cube[1][2][0], cube[1][2][1], cube[1][2][2], cube[5][2][0], cube[5][2][1], cube[5][2][2], cube[3][2][0], \
            cube[3][2][1], cube[3][2][2], cube[4][2][0], cube[4][2][1], cube[4][2][2] = cube[5][2][0], cube[5][2][1], \
                                                                                        cube[5][2][2], cube[3][2][0], \
                                                                                        cube[3][2][1], cube[3][2][2], \
                                                                                        cube[4][2][0], cube[4][2][1], \
                                                                                        cube[4][2][2], cube[1][2][0], \
                                                                                        cube[1][2][1], cube[1][2][2]
    elif front == 3:
        if direc == '+':
            pass
        else:
            pass
    elif front == 4:
        if direc == '+':
            pass
        else:
            pass
    elif front == 5:
        if direc == '+':
            pass
        else:
            pass


def rotate(dimen, direc):
    temp = [['' for __ in range(3)] for _ in range(3)]
    for r in range(3):
        for c in range(3):
            if direc == '+':
                temp[c][2 - r] = cube[dimen][r][c]
            else:
                temp[2 - c][r] = cube[dimen][r][c]
    for r in range(3):
        for c in range(3):
            cube[dimen][r][c] = temp[r][c]


if __name__ == "__main__":
    for _ in range(int(input())):
        n = input()
        operations = input()[:-1].split()
        for oper in operations:
            idx = directions.index(oper[0])
            rotate(idx, oper[1])
            rotate_edges(idx, oper[1])
    for u in cube[0]:
        print(''.join(u))
