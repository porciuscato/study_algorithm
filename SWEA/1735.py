import sys

sys.stdin = open('1735.txt', 'r')


def solve(R, C):
    global answer
    for row in range(1, N):
        for col in range(1, N):
            if C + row < N and R + row + col < N and C - col >= 0 and (row + col) * 2 > answer:
                visited = [False] * 101
                isAble = True
                now_r, now_c = R, C
                idx = 1
                for delta in ((1, 1), (1, -1), (-1, -1), (-1, 1)):
                    for _ in range(row) if idx % 2 else range(col):
                        now_r += delta[0]
                        now_c += delta[1]
                        if not visited[BOARD[now_r][now_c]]:
                            visited[BOARD[now_r][now_c]] = True
                        else:
                            isAble = False
                            break
                    if not isAble:
                        break
                    idx += 1
                if isAble:
                    answer = (row + col) * 2


for T in range(1, int(input()) + 1):
    answer = -1
    N = int(input())
    BOARD = [list(map(int, input().split())) for _ in range(N)]
    for r in range(N):
        for c in range(N):
            solve(r, c)
    print('#{} {}'.format(T, answer))
