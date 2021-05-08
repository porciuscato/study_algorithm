def prim(graph) -> float:
    max_profits = [-2000000000 for _ in range(M)]
    visited = [False for _ in range(N)]
    max_profits[0] = 0

    que = [(0, F, 0, 0)]  # 시간당 이익(-), 남은 비용, 총 시간, 노드
    front = -1
    rear = 0
    while front != rear:
        front += 1
        profit, left_cost, take_time, start = que[front]

        for end, cost, time in graph[start]:
            if not visited[end]:
                value = (left_cost - cost) / (take_time + time)
                if value > max_profits[end]:
                    max_profits[end] = value

                    pass

    return -que[rear][0]


if __name__ == "__main__":
    import sys

    s_input = sys.stdin.readline
    s_print = sys.stdout.write

    N, M, F = map(int, s_input().split())
    data = [[] for _ in range(N)]
    for _ in range(M):
        i, j, c, t = map(int, s_input().split())
        data[i - 1].append((j, c, t))
        data[j - 1].append((i, c, t))

    answer = prim(data)
    if answer < 0:
        s_print('0.0000\n')
    else:
        s_print('{ans:.4f}'.format(ans=answer))


abc = 1 / 3
print('%.4f' % abc)
print('{a:.4f}'.format(a=abc))
