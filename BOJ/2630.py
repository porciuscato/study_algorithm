import sys

input = sys.stdin.readline


def solve(coordinate: tuple, length: int):
    global w_ps, b_ps
    r, c = coordinate
    if length == 1:
        if paper[r][c] == 0:
            w_ps += 1
        else:
            b_ps += 1
    else:
        check = True
        origin = paper[r][c]
        row = r
        col = c
        while row < r + length:
            if paper[row][col] != origin:
                half = length // 2
                coordinates = [(r, c), (r + half, c), (r, c + half), (r + half, c + half)]
                for cor in coordinates:
                    solve(cor, half)
                check = False
                break
            else:
                if col < c + length - 1:
                    col += 1
                else:
                    row += 1
                    col = c
        if check:
            if origin == 0:
                w_ps += 1
            else:
                b_ps += 1


if __name__ == '__main__':
    N = int(input())
    w_ps = 0
    b_ps = 0
    paper = [list(map(int, input().split())) for _ in range(N)]
    solve((0, 0), N)
    print("{}\n{}".format(w_ps, b_ps))
