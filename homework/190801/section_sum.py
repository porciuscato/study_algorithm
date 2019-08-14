# 4835
def f_max(b):
    M = b[0]
    for i in range(1, len(b)):
        if M < b[i]:
            M = b[i]
    return M


def f_min(b):
    m = b[0]
    for i in range(1, len(b)):
        if m > b[i]:
            m = b[i]
    return m


for T in range(1, int(input()) + 1):
    N, M = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = [0 for i in range(N - M + 1)]
    for i in range(len(b)):
        s = 0
        for j in range(M):
            s += a[i + j]
        b[i] = s
    print('#{} {}'.format(T, f_max(b) - f_min(b)))
