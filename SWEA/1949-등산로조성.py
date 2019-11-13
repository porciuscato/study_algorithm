import sys

sys.stdin = open('1949.txt', 'r')


def bfs(rr, cc):
    global ans
    que = [(rr, cc, 1)]
    front = -1
    rear = 0
    mx = 0
    while front != rear:
        front += 1
        t_r, t_c, t_depth = que[front]
        for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            trow = t_r + dr
            tcol = t_c + dc
            depth = t_depth + 1
            if 0 <= trow < N and 0 <= tcol < N and M[t_r][t_c] > M[trow][tcol]:
                que.append((trow, tcol, depth))
                rear += 1
                if depth > mx:
                    mx = depth
    if mx > ans:
        ans = mx


def solve():
    for rr, cc in top:
        bfs(rr, cc)


for T in range(1, int(input()) + 1):
    ans = 0
    N, K = map(int, input().split())
    M = [list(map(int, input().split())) for _ in range(N)]
    top = []
    mx = 0
    for row in range(N):
        for col in range(N):
            if M[row][col] < mx:
                continue
            elif M[row][col] == mx:
                top.append((row, col))
            else:
                mx = M[row][col]
                top = [(row, col)]

    for k in range(K + 1):
        for row in range(N):
            for col in range(N):
                M[row][col] -= k
                solve()
                M[row][col] += k
    print('#{} {}'.format(T, ans))
