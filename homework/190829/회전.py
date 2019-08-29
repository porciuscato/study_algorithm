for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = input().split()
    for i in range(M):
        arr.append(arr.pop(0))
    print('#{} {}'.format(T, arr[0]))
