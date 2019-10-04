import sys

sys.stdin = open('input.txt', 'r')

delta = ((-1, 0), (0, 1), (1, 0), (0, -1))

for T in range(1, int(input()) + 1):
    N = int(input())
    B = [list(map(int, input().split())) for _ in range(N)]
    ans_num = N ** 2
    ans_count = 0
    v = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not v[r][c]:
                v[r][c] = 1
                tr = r
                tc = c
                d = 1
                while True:
                    for i in range(4):
                        rr = tr + delta[i][0]
                        cc = tc + delta[i][1]
                        if 0 <= rr < N and 0 <= cc < N and B[rr][cc] == B[r][c] + 1:
                            d += 1
                            tr = rr
                            tc = cc
                            v[rr][cc] = 1
                    if tr == rr and tc == cc:
                        break
            if d > ans_count:
                ans_count = d
                ans_num = B[r][c]
            elif d == ans_count and B[r][c] < ans_num:
                ans_num = B[r][c]
            else:
                continue
    print('#{} {} {}'.format(T, ans_num, ans_count))
