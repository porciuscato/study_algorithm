import sys

sys.stdin = open('1494.txt', 'r')


# def solve(sub_total, depth, size, visit, last):
#     global vector, answer
#     if depth == size:
#         answer = min(answer, sub_total)
#     else:
#         # for v in range(size):
#         #     if not visit[v]:
#         #         start = v
#         #         break
#         for ii in range(last, size - 1):
#             for jj in range(ii + 1, size):
#                 if not visit[ii] and not visit[jj]:
#                     sub_t = sub_total + vector[ii][jj]
#                     visit[ii] = 1
#                     visit[jj] = 1
#                     solve(sub_t, depth + 2, size, visit, jj)
#                     visit[ii] = 0
#                     visit[jj] = 0
#
#
# for T in range(1, int(input()) + 1):
#     answer = 1e20
#     N = int(input())
#     warms = [list(map(int, input().split())) for _ in range(N)]
#     vector = [[0] * N for _ in range(N)]
#     for i in range(N - 1):
#         for j in range(i + 1, N):
#             a = ((warms[i][0] - warms[j][0]) ** 2) + ((warms[i][1] - warms[j][1]) ** 2)
#             b = ((warms[j][0] - warms[i][0]) ** 2) + ((warms[j][1] - warms[i][1]) ** 2)
#             vector[i][j] = min(a, b)
#
#     visited = [0] * N
#     solve(0, 0, N, visited, 0)
#     print(f'#{T} {answer}')


# ??
def solve(index, p, m, size, sum_x, sum_y):
    global warms, answer, N
    if size == N:
        answer = min(answer, sum_x ** 2 + sum_y ** 2)
    else:
        if p < N // 2:
            solve(index + 1, p + 1, m, size + 1, sum_x + warms[index][0], sum_y + warms[index][1])
        if m < N // 2:
            solve(index + 1, p, m + 1, size + 1, sum_x - warms[index][0], sum_y - warms[index][1])


for T in range(int(input())):
    N = int(input())
    warms = [list(map(int, input().split())) for _ in range(N)]
    answer = 1e20
    solve(0, 0, 0, 0, 0, 0)
    print("#{} {}".format(T + 1, answer))
