# https://programmers.co.kr/learn/courses/30/lessons/43164


def solution(tickets):
    # 전처리
    all_ports = sorted(list(set(sum(tickets, []))))
    ICN = all_ports.pop(all_ports.index('ICN'))
    all_ports.insert(0, ICN)  # ['ICN', 'ATL', 'SFO']
    ports_count = len(all_ports)
    DB = [[0] * ports_count for _ in range(ports_count)]
    for ticket in tickets:
        depart, arrive = ticket
        DB[all_ports.index(depart)][all_ports.index(arrive)] += 1

    # print(DB)
    stack = [0]
    answer = ["ICN"]
    while stack:
        depart = stack.pop()
        for arrive in range(ports_count):
            if depart != arrive and DB[depart][arrive]:
                stack.append(arrive)
                answer.append(all_ports[arrive])
                DB[depart][arrive] -= 1
                break
    return answer


cases = [
    [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]],
    [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]],
]

for case in cases:
    print(solution(case))
# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
