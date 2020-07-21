def solve(visited, distance, row, col):
    global ans
    if distance == K and row == 0 and col == C - 1:
        ans += 1
    elif distance < K:
        visit = []
        for i in range(R):  
            temp = []
            for j in range(C):
                temp.append(visited[i][j])
            visit.append(temp)
        for dr, dc in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            nr = row + dr
            nc = col + dc
            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != 'T' and not visit[nr][nc]:
                visit[nr][nc] = True
                solve(visit, distance + 1, nr, nc)
                visit[nr][nc] = False


def main():
    global ans
    if K < R + C - 1:
        ans = 0
    else:
        visited = [[False for _ in range(C)] for __ in range(R)]
        visited[R - 1][0] = True
        solve(visited, 1, R - 1, 0)


if __name__ == "__main__":
    R, C, K = map(int, input().split())
    board = [input() for _ in range(R)]
    ans = 0
    main()
    print(ans)
