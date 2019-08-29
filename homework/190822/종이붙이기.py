result = [1, 3]

for T in range(1, int(input()) + 1):
    N = int(input()) // 10
    while N > len(result):
        result.append(result[-2] * 2 + result[-1])
    print('#{} {}'.format(T, result[N - 1]))
