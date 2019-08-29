for T in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    network = {}
    visited = {}
    for i in range(E):
        f, t = map(int, input().split())
        if not network.get(f):
            network[f] = [t]
        else:
            network[f].append(t)
        if not network.get(t):
            network[t] = [f]
        else:
            network[t].append(f)
        if not visited.get(f):
            visited[f] = 0
        if not visited.get(t):
            visited[t] = 0
    start, end = map(int, input().split())

    que = []
    que.append([start, 0])
    visited[start] = 1
    flag = 0
    while que:
        temp = que.pop(0)
        for node in network[temp[0]]:
            if not visited[node]:
                visited[node] = 1
                depth = temp[1] + 1
                if node == end:
                    flag = depth
                    break
                else:
                    que.append([node, depth])
        if flag:
            break

    print('#{} {}'.format(T, flag))
