import sys

sys.stdin = open('input.txt', 'r')


# def permu(arr, depth, tot):
#     global ans, vis
#     if depth == N:
#         t = tot + abs(cust[arr[-1]][0] - home[0]) + abs(cust[arr[-1]][1] - home[1])
#         if ans > t:
#             ans = t
#     else:
#         for i in range(N):
#             if not vis[i]:
#                 ar = arr[:]
#                 ar += [i]
#                 if depth == 0:
#                     t = tot + abs(cust[i][0] - com[0]) + abs(cust[i][1] - com[1])
#                 else:
#                     t = tot + abs(cust[ar[-1]][0] - cust[i][0]) + abs(cust[ar[-1]][1] - cust[i][1])
#                 if t >= ans:
#                     continue
#                 vis[i] = 1
#                 permu(ar, depth + 1, t)
#                 vis[i] = 0

def permu(last, depth, tot):
    global ans, vis
    if depth == N:
        t = tot + abs(cust[last][0] - home[0]) + abs(cust[last][1] - home[1])
        if ans > t:
            ans = t
    else:
        for i in range(N):
            if not vis[i]:
                if depth == 0:
                    t = tot + abs(cust[i][0] - com[0]) + abs(cust[i][1] - com[1])
                else:
                    t = tot + abs(cust[last][0] - cust[i][0]) + abs(cust[last][1] - cust[i][1])
                if t >= ans:
                    continue
                vis[i] = 1
                permu(i, depth + 1, t)
                vis[i] = 0


for T in range(1, int(input()) + 1):
    N = int(input())
    d = list(map(int, input().split()))
    com = (d[0], d[1])
    home = (d[2], d[3])
    cust = []
    for i in range(4, 2 * (N + 2), 2):
        cust += [(d[i], d[i + 1])]
    ans = 1e5
    vis = [0] * N
    permu(0, 0, 0)
    print('#{} {}'.format(T, ans))
