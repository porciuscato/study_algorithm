import sys
import time

sys.stdin = open('input.txt', 'r')


def solve(depth, tot):
    global ans
    if depth >= 12:
        if tot < ans:
            ans = tot
    else:
        if tot >= ans:
            return
        solve(depth + 1, tot + d1 * month[depth])
        solve(depth + 1, tot + m1)
        solve(depth + 3, tot + m3)


for T in range(1, int(input()) + 1):
    d1, m1, m3, y1 = map(int, input().split())
    month = list(map(int, input().split()))
    ans = y1
    solve(0, 0)
    print('#{} {}'.format(T, ans))
