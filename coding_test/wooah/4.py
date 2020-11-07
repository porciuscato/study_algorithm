from collections import deque


def solution(n, board):
    answer = 0
    cursor = [0, 0]
    for num in range(1, n * n + 1):
        visited = [[False for __ in range(n)] for _ in range(n)]
        que = deque([(cursor, 0)])
        visited[cursor[0]][cursor[1]] = True
        while que:
            tcur, dist = que.popleft()
            r, c = tcur
            if board[r][c] == num:
                answer += dist + 1
                cursor = [r, c]
                board[r][c] = 0
                break
            else:
                for dr, dc in ((0, -1), (-1, 0), (0, 1), (1, 0)):
                    nr, nc = r + dr, c + dc
                    nr = (nr + n) % n
                    nc = (nc + n) % n
                    if not visited[nr][nc]:
                        que.append(([nr, nc], dist + 1))
                        visited[nr][nc] = True
    return answer


cases = [
    (3, [[3, 5, 6], [9, 2, 7], [4, 1, 8]]),
    (2, [[2, 3], [4, 1]]),
    (4, [[11, 9, 8, 12], [2, 15, 4, 14], [1, 10, 16, 3], [13, 7, 5, 6]])
]

for case in cases:
    print(solution(*case))
