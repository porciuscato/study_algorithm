for T in range(1, int(input()) + 1):
    N = float(input())
    result = []
    count = 0
    while N != 0:
        count += 1
        N = N * 2
        if N >= 1:
            result += ['1']
            N = N - 1
        else:
            result += ['0']
        if count == 13:
            result = ['overflow']
            break

    print('#{} {}'.format(T, ''.join(result)))
