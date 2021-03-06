import sys

sys.stdin = open('14503.txt')

delta = ((-1, 0), (0, 1), (1, 0), (0, -1))

N, M = map(int, input().split())
now_r, now_c, now_d = map(int, input().split())
TABLE = [list(map(int, input().split())) for _ in range(N)]
cleared = [[0] * M for _ in range(N)]

ANSWER = 0
back_going = True
while back_going:
    if not cleared[now_r][now_c]:
        cleared[now_r][now_c] = 1
        ANSWER += 1
    for _ in range(4):
        now_d = (now_d + 3) % 4
        next_r = now_r + delta[now_d][0]
        next_c = now_c + delta[now_d][1]
        if not TABLE[next_r][next_c] and not cleared[next_r][next_c]:
            now_r = next_r
            now_c = next_c
            break
    else:
        back_r = now_r - delta[now_d][0]
        back_c = now_c - delta[now_d][1]
        if not TABLE[back_r][back_c]:
            now_r = back_r
            now_c = back_c
        else:
            back_going = False

print(ANSWER)
