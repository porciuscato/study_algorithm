for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    cheese = [[i + 1, data[i]] for i in range(M)]
    idx = -1
    oven = [0] * N
    last = 0

    while True:
        idx += 1
        idx = idx % N
        if oven[idx] == 0:
            if cheese:
                oven[idx] = cheese.pop(0)
            else:
                oven[idx] = 0
        else:
            oven[idx][1] //= 2
            if oven[idx][1] == 0:
                if cheese:
                    oven[idx] = cheese.pop(0)
                else:
                    oven[idx] = 0
        if oven.count(0) == N - 1 and not cheese:
            for i in oven:
                if i:
                    last = i[0]
                    break
            break

    print('#{} {}'.format(T, last))
