# 완주하지 못한 선수

def solution(participant, completion):
    check = [0] * len(participant)
    for comple in completion:
        for idx, parti in enumerate(participant):
            if not check[idx]:
                if comple == parti:
                    check[idx] = 1
                    break
    for idx, value in enumerate(check):
        if value == 0:
            answer = participant[idx]
    return answer


def solution2(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    for idx, value in enumerate(completion):
        if participant[idx] != completion[idx]:
            answer = participant[idx]
            break
    else:
        answer = participant[-1]
    return answer


print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
