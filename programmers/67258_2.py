def solution(gems):
    selected_gems = {}
    size = len(set(gems))

    answer = [1, len(gems)]
    front = 0
    for rear in range(len(gems)):
        selected_gems[gems[rear]] = selected_gems.setdefault(gems[rear], 0) + 1
        while selected_gems.setdefault(gems[front], 0) > 1:
            selected_gems[gems[front]] -= 1
            front += 1
        if len(selected_gems) == size and answer[1] - answer[0] > rear - front:
            answer[0] = front + 1
            answer[1] = rear + 1
    return answer


cases = [
    ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],
    ["AA", "AB", "AC", "AA", "AC"],
    ["XYZ", "XYZ", "XYZ"],
    ["ZZZ", "YYY", "NNNN", "YYY", "BBB"],
    ["a", 'b', 'b', 'a', 'b', 'c', 'a'],
    ["DIA", "EM", "EM", "RUB", "DIA"]
]

for case in cases:
    print(solution(case))
