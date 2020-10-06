import sys

input = sys.stdin.readline
delta = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))


def move_fishes(pbowl):
    for n in range(1, 17):
        i = 0
        j = 0
        find = False
        while i < 4:
            if pbowl[i][j]:
                if pbowl[i][j][0] == n and pbowl[i][j][4] == 0:
                    fish = pbowl[i][j]
                    find = True
                    break
            j += 1
            if j == 4:
                i += 1
                j = 0
        if find:
            cd = fish[3]
            cr = fish[1]
            cc = fish[2]
            for i in range(8):
                nd = (cd + i) % 8
                nr = cr + delta[nd][0]
                nc = cc + delta[nd][1]
                if 0 <= nr < 4 and 0 <= nc < 4:
                    if pbowl[nr][nc] == 0:
                        fish[1] = nr
                        fish[2] = nc
                        fish[3] = nd
                        pbowl[nr][nc] = fish
                        pbowl[cr][cc] = 0
                        break
                    elif pbowl[nr][nc][4] == 0:
                        t_fish = pbowl[nr][nc]
                        fish[1] = nr
                        fish[2] = nc
                        fish[3] = nd
                        t_fish[1] = cr
                        t_fish[2] = cc
                        pbowl[cr][cc] = t_fish
                        pbowl[nr][nc] = fish
                        break


def solve(score, srow, scol, pbowl):
    global ans
    score += pbowl[srow][scol][0]
    shark = [score, srow, scol, pbowl[srow][scol][3], 1]
    pbowl[srow][scol] = shark
    ans = max(score, ans)
    move_fishes(pbowl)
    sr = shark[1]
    sc = shark[2]
    sd = shark[3]
    m = 1
    while 1:
        nr = sr + (delta[sd][0] * m)
        nc = sc + (delta[sd][1] * m)
        if 0 <= nr < 4 and 0 <= nc < 4:
            if pbowl[nr][nc] != 0:
                bbowl = [[0 for _ in range(4)] for __ in range(4)]
                for i in range(4):
                    for j in range(4):
                        if pbowl[i][j]:
                            bbowl[i][j] = pbowl[i][j][:]
                bbowl[sr][sc] = 0
                solve(score, nr, nc, bbowl)
        else:
            break
        m += 1


if __name__ == "__main__":
    fishbowl = [[[] for _ in range(4)] for __ in range(4)]
    for i in range(4):  
        inp = list(map(int, input().split()))
        for j in range(0, 8, 2):
            fishbowl[i][j // 2] = [inp[j], i, j // 2, inp[j + 1] - 1, 0]
    ans = 0
    solve(0, 0, 0, fishbowl)
    print(ans)
