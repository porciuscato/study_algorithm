import sys

sys.stdin = open('5658.txt', 'r')

for T in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    NUMBER = list(input())
    ROTATE = N // 4
    numbers = []
    for rotate in range(ROTATE):
        NUMBER.append(NUMBER.pop(0))
        for r in range(4):
            part = NUMBER[ROTATE * r : ROTATE * (r + 1)]
            numbers.append(''.join(part))
    numbers = sorted(list(set(numbers)))[::-1]
    answer = int(numbers[K - 1], 16)
    print('#{} {}'.format(T, answer))
