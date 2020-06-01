array = [0] * 60001
array[1] = 1
array[2] = 2
for i in range(3, 60001):
    array[i] = array[i - 1] + array[i - 2]


def solution(n):
    return array[n] % 1000000007


problems = [
    4
]

for p in problems:
    print(solution(p))
