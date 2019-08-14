# 4831
def test(K, N, M, stop, jido):
    if (M < N // K) or (stop[0] > K) or (N - stop[-1] > K):
        return 0
    for i in range(len(stop) - 1):
        if stop[i + 1] - stop[i] > K:
            return 0
    now, count = 0, 0
    while True:
        if now + K >= N:
            break
        for i in range(K, 0, -1):
            if jido[now + i] == 1:
                now += i
                count += 1
                break
    return count


for T in range(1, int(input()) + 1):
    K, N, M = list(map(int, input().split()))
    stop = list(list(map(int, input().split())))
    jido = [0 for i in range(N+K)]
    for i in stop:
        jido[i] = 1
    result = test(K, N, M, stop, jido)
    print('#{} {}'.format(T, result))
