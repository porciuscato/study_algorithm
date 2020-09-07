import sys

input = sys.stdin.readline


def solve(coordinate: tuple, length: int):
    global ans
    row, col = coordinate
    if length == 1:
        ans += video[row][col]
    else:
        pos = True
        origin = video[row][col]
        r, c = row, col
        while r < row + length:
            if video[r][c] != origin:
                pos = False
                break
            else:
                if c < col + length - 1:
                    c += 1
                else:
                    r += 1
                    c = col
        if pos:
            ans += origin
        else:
            half = length // 2
            coordinates = [(row, col), (row, col + half), (row + half, col), (row + half, col + half)]
            ans += "("
            for cor in coordinates:
                solve(cor, half)
            ans += ")"


if __name__ == '__main__':
    N = int(input())
    video = [list(input()) for _ in range(N)]
    ans = ""
    solve((0, 0), N)
    print(ans)
