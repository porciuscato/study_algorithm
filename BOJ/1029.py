def solve(_now, value, visited):
    global ans
    pos = False
    for i in range(N):
        if _now != i and board[_now][i] >= value:
            vis = visited[:]
            vis[i] = 1
            solve(i, board[_now][i], vis)
            pos = True
    result = sum(visited)
    if not pos or result == N:
        ans = max(ans, result)


def main():
    value = 0
    visited = [0] * N
    visited[0] = 1
    solve(0, value, visited)


if __name__ == "__main__":
    ans = 0
    N = int(input())
    board = [list(map(int, list(input()))) for _ in range(N)]
    main()
    print(ans)
