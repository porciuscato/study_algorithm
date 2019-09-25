def select(a, depth, tot):
    global mini
    visited[a] = 1
    if depth == N - 1:
        t = tot + base[a][0]
        if t < mini:
            mini = t
        return
    for i in range(N):
        if not visited[i]:
            select(i, depth + 1, tot + base[a][i])
            visited[i] = 0


for T in range(1, int(input()) + 1):
    N = int(input())
    base = [list(map(int, input().split())) for _ in range(N)]
    mini = 9999999
    visited = [0] * N
    select(0, 0, 0)
    print('#{} {}'.format(T, mini))
