phone = {}


def get_distance(coor, num):
    sr, sc = phone[coor]
    dr, dc = phone[num]
    return abs(sr - dr) + abs(sc - dc)


def solution(numbers, hand):
    global phone
    idx = 1
    for i in range(4):
        for j in range(3):
            phone[idx] = (i, j)
            idx += 1

    answer = ''
    left = 10
    right = 12
    for num in numbers:
        num = 11 if num == 0 else num
        if num in (1, 4, 7):
            answer += 'L'
            left = num
        elif num in (3, 6, 9):
            answer += 'R'
            right = num
        else:
            l_dis = get_distance(left, num)
            r_dis = get_distance(right, num)
            if hand == 'left':
                if l_dis <= r_dis:
                    answer += 'L'
                    left = num
                else:
                    answer += 'R'
                    right = num
            else:
                if l_dis >= r_dis:
                    answer += 'R'
                    right = num
                else:
                    answer += 'L'
                    left = num
    return answer


cases = [
    ([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"),
    ([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"),
    ([2], "right"),
    ([2], "left"),
]

for case in cases:
    print(solution(*case))
