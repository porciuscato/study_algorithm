for T in range(1, int(input()) + 1):
    N = int(input())
    base = [list(map(int, input().split())) for _ in range(N)]
    mini = 0
    for i in range(N):
        mini += base[i][i]

    visited = [0] * N
    def select(visited, depth, tot):
        global mini
        if depth == N:
            if tot < mini:
                mini = tot
            return
        else:
            for i in range(N):
                if not visited[i]:
                    adder = tot + base[depth][i]
                    if adder > mini:
                        continue
                    else:
                        visited[i] = 1
                        select(visited, depth + 1, adder)
                        visited[i] = 0
    select(visited, 0, 0)
    print('#{} {}'.format(T, mini))
