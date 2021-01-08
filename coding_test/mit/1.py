def solution(openA, closeB):
    array = sorted([(i, 'A') for i in openA] + [(i, 'B') for i in closeB])
    answer = 0
    started = False
    start_time = 0
    for ele in array:
        if not started and ele[1] == 'A':
            start_time = ele[0]
            started = True
        elif started and ele[1] == 'B':
            started = False
            answer += ele[0] - start_time
            start_time = 0
    return answer


cases = [
    ([3, 5, 7], [4, 10, 12]),
    ([4, 7, 9, 16], [2, 5, 12, 14, 20])
]

for case in cases:
    print(solution(*case))
