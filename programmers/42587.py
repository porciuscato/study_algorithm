def is_printed(value, arr):
    for i in range(len(arr)):
        if value < arr[i]:
            return False
    return True


def solution(priorities, location):
    answer = 1
    pos = location
    while True:
        first = priorities.pop(0)
        printed = is_printed(first, priorities)
        if printed and pos == 0:
            return answer
        elif printed and pos != 0:
            answer += 1
            pos -= 1
        elif not printed and pos == 0:
            priorities.append(first)
            pos = len(priorities) - 1
        else:
            priorities.append(first)
            pos -= 1


print(solution([1, 1, 9, 1, 1, 1], 0))
