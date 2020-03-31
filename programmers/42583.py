def solution(bridge_length, weight, truck_weights):
    answer = 0
    head = 0
    now = 0
    _len = len(truck_weights)
    check = [0] * _len
    while head < _len:
        answer += 1
        for idx in range(head, head + bridge_length):
            if idx == _len:
                break
            if (idx - 1) != -1 and check[idx - 1] == 1:
                break
            if check[idx] == 0:
                now += truck_weights[idx]
            if now <= weight:
                check[idx] += 1
                if check[idx] == bridge_length + 1:
                    now -= truck_weights[head]
                    head += 1
            else:
                now -= truck_weights[idx]
                break
    return answer


# print(solution(2, 10, [7, 4, 5, 6]))
# print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
