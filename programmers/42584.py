def solution(prices):
    answer = []
    _len = len(prices)
    for i in range(_len - 1):
        tot = 1
        for j in range(i + 1, _len - 1):
            if prices[i] <= prices[j]:
                tot += 1
            else:
                break
        answer.append(tot)
    answer.append(0)
    return answer


print(solution([1, 2, 3, 2, 3]))
