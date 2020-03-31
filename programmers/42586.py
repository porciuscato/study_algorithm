def solution(progresses, speeds):
    answer = []
    length = len(progresses)
    index = 0
    deploy = 0
    while index < length:
        for i in range(index, length):
            if progresses[i] >= 100:
                index += 1
                deploy += 1
            else:
                break
        if deploy:
            answer.append(deploy)
            deploy = 0
        for j in range(index, length):
            progresses[j] += speeds[j]
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
