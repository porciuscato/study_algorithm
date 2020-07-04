from collections import deque
import sys

input = sys.stdin.readline


def check_visit(row, col, field, visited, M, N):
    que = deque([(row, col)])
    visited[row][col] = True
    while que:
        x, y = que.popleft()
        for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and field[nx][ny] and not visited[nx][ny]:
                que.append((nx, ny))
                visited[nx][ny] = True


def main():
    for T in range(int(input())):
        M, N, K = map(int, input().split())
        field = [[0 for _ in range(M)] for __ in range(N)]
        for k in range(K):
            x, y = map(int, input().split())
            field[y][x] = 1
        # BFS
        ans = 0
        visited = [[False for _ in range(M)] for __ in range(N)]
        for row in range(N):
            for col in range(M):
                if field[row][col] and not visited[row][col]:
                    check_visit(row, col, field, visited, M, N)
                    ans += 1
        print(ans)


main()
