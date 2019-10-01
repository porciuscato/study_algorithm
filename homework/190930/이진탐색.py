def search(b):
    L = 0
    R = N - 1
    d = -1
    while True:
        M = (L + R) // 2
        if A[M] == b:
            return 1
        if L == R:
            return 0
        if b < A[M]:
            if d == 0:
                return 0
            d = 0
            R = M - 1
        else:
            if d == 1:
                return 0
            d = 1
            L = M + 1


for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    ans = 0
    for b in B:
        ans += search(b)
    print('#{} {}'.format(T, ans))