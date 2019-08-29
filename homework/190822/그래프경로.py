for T in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    board = [[0] * (V + 1) for _ in range(V + 1)]
    stack = []
    visited = [0] * (V + 1)
    result = 0
    for i in range(E):
        x, y = map(int, input().split())
        board[x][y] = 1
    start, end = map(int, input().split())


    def dfs(start):
        global result
        for i in range(1, V + 1):
            if board[start][i]:
                dfs(i)
                if i == end:
                    result = 1
                visited[i] = 1

    dfs(start)

    print('#{} {}'.format(T, result))
