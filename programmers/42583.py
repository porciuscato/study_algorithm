# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     head = 0
#     now = 0
#     _len = len(truck_weights)
#     check = [0] * _len
#     while head < _len:
#         answer += 1
#         for idx in range(head, head + bridge_length):
#             if idx == _len:
#                 break
#             if (idx - 1) != -1 and check[idx - 1] == 1:
#                 break
#             if check[idx] == 0:
#                 now += truck_weights[idx]
#             if now <= weight:
#                 check[idx] += 1
#                 if check[idx] == bridge_length + 1:
#                     now -= truck_weights[head]
#                     head += 1
#             else:
#                 now -= truck_weights[idx]
#                 break
#     return answer


def solution(bridge_length, weight, truck_weights):
    answer = 0
    now_weight = 0
    _len = len(truck_weights)
    finished = 0
    bridge = [0] * bridge_length
    while finished < _len:
        answer += 1
        out = bridge.pop(0)
        if out:
            now_weight -= out
            finished += 1
        if truck_weights:
            in_check = truck_weights[0]
            if now_weight + in_check <= weight:
                new_truck = truck_weights.pop(0)
                bridge.append(new_truck)
                now_weight += new_truck
            else:
                bridge.append(0)
        else:
            bridge.append(0)
    return answer


# print(solution(2, 10, [7, 4, 5, 6]))
# print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
