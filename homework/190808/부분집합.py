A = [i for i in range(1, 13)]

for T in range(1, int(input()) + 1):
    count = 0
    N, K = map(int, input().split())
    size = len(A)

    for i in range(1, 1 << size):
        temp = []
        for j in range(size):
            if i & (1 << j):
                temp.append(A[j])
        if len(temp) == N:
            if sum(temp) == K:
                count += 1
    print('#{} {}'.format(T, count))