import sys

sys.stdin = open('input.txt', 'r')

for T in range(1, int(input()) + 1):
    N = int(input())
    base = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    # 최소이므로? 최소여도 DFS 가능하지

    def dfs(start, tot):
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                hap = tot + base[start][i]
                dfs(i, hap)

    visited[0] = 1
    dfs(0, 0)

    print('#{} {}'.format(T, 0))
