# https://programmers.co.kr/learn/courses/30/lessons/43162


# def solution(n, computers):
#     answer = 0
#     visited = [[0] * n for _ in range(n)]
#     delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
#     for i in range(n):
#         for j in range(n):
#             if computers[i][j] and not visited[i][j]:
#                 answer += 1
#                 que = []
#                 visited[i][j] = 1
#                 que.append((i, j))
#                 while que:
#                     x, y = que.pop(0)
#                     for d_x, d_y in delta:
#                         dx = x + d_x
#                         dy = y + d_y
#                         if 0 <= dx < n and 0 <= dy < n and computers[dx][dy] and not visited[dx][dy]:
#                             visited[dx][dy] = 1
#                             que.append((dx, dy))
#     return answer


def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            answer += 1
            stack = list()
            stack.append(i)
            while stack:
                check = stack.pop()
                for j in range(n):
                    if check != j and computers[check][j] and not visited[j]:
                        stack.append(j)
                        visited[j] = 1
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
