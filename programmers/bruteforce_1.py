def solution(answers):
    answer = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    length = len(answers)
    for i in range(len(answer)):
        answer[i] = answer[i] * ((length // len(answer[i])) + 1)
    ans_list = [0, 0, 0]
    for i in range(length):
        for num in range(3):
            if answers[i] == answer[num][i]:
                ans_list[num] += 1
    mx = max(ans_list)
    answer = []
    for i in range(3):
        if mx == ans_list[i]:
            answer.append(i + 1)
    return answer
