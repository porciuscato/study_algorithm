INF = 4 * (10 ** 10)


def search(costs, graph, node):
    leader = costs[node]
    member = 0
    leaves = []
    if not graph[node]:
        return leader, INF
    for leaf in graph[node]:
        leaves.append(search(costs, graph, leaf))
    for leaf in leaves:
        if leaf[1] != INF:
            leader += min(leaf[0], leaf[1])
    mnValue, mnDiffer = INF, INF
    onlyLeaves, flag = True, False
    for leaf in leaves:
        if leaf[1] != INF:
            onlyLeaves = False
            if leaf[0] <= leaf[1]:
                flag = True
            else:
                mnDiffer = min(mnDiffer, leaf[0] - leaf[1])
            member += min(leaf[0], leaf[1])
        else:
            mnValue = min(mnValue, leaf[0])

    if onlyLeaves:
        member = mnValue
    else:
        if not flag:
            if onlyLeaves:
                member += mnDiffer
            else:
                member += min(mnDiffer, mnValue)
    return leader, member


def solution(sales, links):
    costs = [0] + sales[:]
    graph = [[] for _ in range(len(sales) + 1)]
    for s, e in links:
        graph[s].append(e)
    return min(search(costs, graph, 1))


cases = [
    ([14, 17, 15, 18, 19, 14, 13, 16, 28, 17],
     [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]),
    ([5, 6, 5, 3, 4], [[2, 3], [1, 4], [2, 5], [1, 2]]),
    ([5, 6, 5, 1, 4], [[2, 3], [1, 4], [2, 5], [1, 2]]),
    ([10, 10, 1, 1], [[3, 2], [4, 3], [1, 4]]),
]

for case in cases:
    print(solution(*case))
