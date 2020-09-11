from itertools import permutations


def solution(n, weak, dist):
    answer = -1
    dist.sort()
    dist = dist[::-1]
    length = len(weak)
    weak = weak + [(weak[i] + n) for i in range(length - 1)]

    for ans in range(1, len(dist) + 1):
        friends = permutations(dist[:ans], ans)
        for friend in friends:
            front = 0
            rear = length
            while front < length:
                fri_start = 0
                cleared = [0] * 2 * length
                idx = front
                while fri_start < ans:
                    criteria = weak[idx] + friend[fri_start]
                    while weak[idx] <= criteria:
                        cleared[idx] = 1
                        idx += 1
                    fri_start += 1
                if sum(cleared) == length:
                    return ans
                front += 1
                rear += 1
    return answer


cases = (
    (12, [1, 5, 6, 10], [1, 2, 3, 4]),
    (12, [1, 3, 4, 9, 10], [3, 5, 7]),
    (200, [0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30])
)

for case in cases:
    print(solution(*case))
