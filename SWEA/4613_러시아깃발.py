import sys

sys.stdin = open('4613.txt')


def solve(array, row, col):
    global answer
    first, second = array
    NEW_FLAG = []
    for i1 in range(0, first + 1):
        NEW_FLAG.append('W' * col)
    for i2 in range(first + 1, second + 1):
        NEW_FLAG.append('B' * col)
    for i3 in range(second + 1, row):
        NEW_FLAG.append('R' * col)
    result = 0
    for r in range(row):
        for c in range(col):
            if ORIGIN[r][c] != NEW_FLAG[r][c]:
                result += 1
    answer = min(answer, result)


def combination(array, depth, last, row, col):
    if depth == 2:
        solve(array, row, col)
    else:
        for i in range(last, row - 1):
            arr = array[:]
            arr.append(i)
            combination(arr, depth + 1, i + 1, row, col)


for T in range(1, int(input()) + 1):
    answer = 1e10
    ROW, COL = map(int, input().split())
    ORIGIN = [input() for _ in range(ROW)]
    combination([], 0, 0, ROW, COL)
    print('#{} {}'.format(T, answer))

