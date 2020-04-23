import sys

sys.stdin = open('1494.txt', 'r')


def permu(arr, depth, size, vis):
    global answer, warms
    if depth == size:
        temp = 0
        # for j in range(0, size, 2):
        #     a = warms[j]
        #     b = warms[j + 1]
        #     temp += ((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2)
        answer = int(min(answer, temp))
    else:
        for i in range(N):
            if not vis[i]:
                if depth % 2 and i < arr[depth - 1]:
                    return
                ar = arr[:]
                ar.append(i)
                vis[i] = 1
                permu(ar, depth + 1, size, vis)
                vis[i] = 0


for T in range(1, int(input()) + 1):
    answer = 1e30
    N = int(input())
    warms = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    permu([], 0, N, visited)
    print(f'#{T} {answer}')
