import sys

sys.stdin = open('input.txt', 'r')

delta = ((-1, 0), (0, 1), (1, 0), (0, -1))


def dfs(r, c):
    global ans
    stack = []
    stack += [(r, c, 1, [board[r][c]])]
    while stack:
        tr, tc, td, tarr = stack.pop(-1)
        for i in range(4):
            dr = tr + delta[i][0]
            dc = tc + delta[i][1]
            if 0 <= dr < 4 and 0 <= dc < 4:
                dd = td + 1
                darr = tarr + [board[dr][dc]]
                if dd == 7:
                    ans += [int(''.join(darr))]
                else:
                    stack += [(dr, dc, dd, darr)]


for T in range(1, int(input()) + 1):
    board = [input().split() for _ in range(4)]
    ans = []
    for r in range(4):
        for c in range(4):
            dfs(r, c)
    print('#{} {}'.format(T, len(set(ans))))
