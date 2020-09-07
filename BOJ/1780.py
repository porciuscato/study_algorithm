import sys

input = sys.stdin.readline


def solve(coor: tuple, leng: int):
    global p_m, p_z, p_p
    R, C = coor
    if leng == 1:
        p = paper[R][C]
        if p == -1:
            p_m += 1
        elif p == 0:
            p_z += 1
        elif p == 1:
            p_p += 1
    else:
        pos = True
        origin = paper[R][C]
        r, c = R, C
        while r < R + leng:
            if paper[r][c] != origin:
                pos = False
                break
            else:
                if c < C + leng - 1:
                    c += 1
                else:
                    r += 1
                    c = C
        if pos:
            solve(coor, 1)
        else:
            t = leng // 3
            dt = 2 * t
            coors = [(R, C), (R, C + t), (R, C + dt),
                     (R + t, C), (R + t, C + t), (R + t, C + dt),
                     (R + dt, C), (R + dt, C + t), (R + dt, C + dt)]
            for cor in coors:
                solve(cor, t)


if __name__ == '__main__':
    N = int(input())
    paper = [list(map(int, input().split())) for _ in range(N)]
    p_m, p_z, p_p = 0, 0, 0
    solve((0, 0), N)
    print("{}\n{}\n{}".format(p_m, p_z, p_p))
