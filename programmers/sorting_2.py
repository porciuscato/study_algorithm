def solution(numbers):
    length = len(numbers)
    numbers.append(-1)  # index 처리를 위한 방책
    numbers = list(map(str, numbers))
    ordered = sorted(numbers, key=lambda x: x[0], reverse=True)
    # print(ordered)
    temp, start, end = [], -1, -1
    for idx in range(length):
        if numbers[idx][0] == numbers[idx + 1][0]:
            temp.append(numbers[idx])
            if start < 0:
                start = idx
        elif temp:
            if end < 0:
                end = idx
            temp.append(numbers[idx])
            # 여기서 처리해야지
            print(temp)
            # 처리처리
            ordered[start: end + 1] = temp
            temp, start, end = [], -1, -1
    answer = ''.join(ordered[0:-1])
    return answer


# print(solution([3, 30, 34, 5, 9]))
print(solution([6, 10, 2, 1, 3, 4, 5, 7, 8, 9, 123, 3, 31, 30, 325, 342, 325, 325, 321, 37, 397]))
