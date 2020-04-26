def solution(s):
    length = len(s)
    mx = length // 2
    answer = 10000 if mx != 0 else 1
    for compress in range(1, mx + 1):
        result = []
        start_i = 0
        size = 0
        while start_i < length:
            result.append(s[start_i:start_i + compress])
            start_i += compress
            size += 1
        sub_total = 0
        start = 0
        while start < size:
            check = result[start]
            number = 0
            fix_start = start
            for idx in range(fix_start, size):
                if check == result[idx]:
                    number += 1
                else:
                    break
            sub_total += len(check) if number == 1 else len(str(number)) + compress
            start += 1 if number == 1 else number
        answer = min(answer, sub_total)
    return answer


arr = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",
    "abababaaaaaaaa",
    "a"
]

for ar in arr:
    print('answer is {}'.format(solution(ar)))
