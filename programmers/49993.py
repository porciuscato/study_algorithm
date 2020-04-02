_all = {}
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXZY'
start = 0
for ch in chars:
    _all[ch] = start
    start += 1


def solution(skill, skill_trees):
    answer = 0
    skill_index = [-1] * len(chars)
    order = 1
    for sk in skill:
        skill_index[_all[sk]] = order
        order += 1
    for skill_set in skill_trees:
        right_order = 1
        for one in skill_set:
            value = skill_index[_all[one]]
            if value == -1:
                continue
            elif value == right_order:
                right_order += 1
            else:
                break
        else:
            answer += 1
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
