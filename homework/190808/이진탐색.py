for T in range(1, int(input()) + 1):
    P, A, B = list(map(int, input().split()))

    l, r, count_A = 1, P, 1
    while True:
        c = int((l + r) / 2)
        if c == A:
            break
        elif c < A:
            l = c
            count_A += 1
        else:
            r = c
            count_A += 1

    l, r, count_B = 1, P, 1
    while True:
        c = int((l + r) / 2)
        if c == B:
            break
        elif c < B:
            l = c
            count_B += 1
        else:
            r = c
            count_B += 1
    if count_A < count_B:
        result = 'A'
    elif count_A > count_B:
        result = 'B'
    else:
        result = 0
    print('#{} {}'.format(T, result))