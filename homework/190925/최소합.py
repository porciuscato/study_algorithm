dt = ((0, 1), (1, 0))
def rc(r, c, t):
    global mn
    if r == N - 1 and c == N - 1:
        if t < mn: mn = t
    else:
        for i in range(2):
            dr = r + dt[i][0]
            dc = c + dt[i][1]
            if 0 <= dr < N and 0 <= dc < N:
                tt = t + B[dr][dc]
                if tt > mn: continue
                rc(dr, dc, tt)
for T in range(1, int(input()) + 1):
    N = int(input())
    B = [list(map(int, input().split())) for _ in range(N)]
    mn = 9999999999
    rc(0, 0, B[0][0])
    print('#{} {}'.format(T, mn))
