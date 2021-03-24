airports, DB, answer = [], [], ["ICN"]


def dfs(depart):
    global airports, DB, answer
    find = False
    for i in range(len(airports)):
        if DB[depart][i]:
            find = True
            DB[depart][i] -= 1
            answer.append(airports[i])
            if dfs(i):
                return True
            answer.pop()
            DB[depart][i] += 1
            find = False
    if not find:
        for i in range(len(airports)):
            for j in range(len(airports)):
                if DB[i][j]:
                    return False
        return True


def solution(tickets):
    global airports, DB, answer
    airports, DB, answer = [], [], ["ICN"]
    airports = sorted(list(set(sum(tickets, []))))
    ICN = airports.index('ICN')
    DB = [[0] * len(airports) for _ in range(len(airports))]
    for ticket in tickets:
        depart, arrive = ticket
        DB[airports.index(depart)][airports.index(arrive)] += 1
    dfs(ICN)
    return answer


cases = [
    [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]],
    [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]],
    [['ICN', 'B'], ['B', 'ICN'], ['ICN', 'A'], ['A', 'D'], ['D', 'A']],  # ['ICN', 'B', 'ICN', 'A', 'D', 'A']
]

for case in cases:
    print(solution(case))
