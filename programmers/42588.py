def solution(heights):
    answer = []
    _len = len(heights)
    for i in range(_len - 1, 0, -1):
        now = heights[i]
        for j in range(i - 1, -1, -1):
            if now < heights[j]:
                answer.insert(0, j + 1)
                break
        else:
            answer.insert(0, 0)
    answer.insert(0, 0)
    return answer
