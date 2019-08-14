def combination(arr, N):
    for i in range(N):
        if i%2:
            mini = arr[i]
            for j in range(i+1,N):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                    mini = arr[j]
        else:
            maxi = arr[i]
            for j in range(i+1,N):
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
                    maxi = arr[j]
    return arr

for T in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int,input().split()))
    result = combination(arr, N)
    print('#{} {}'.format(T, ' '.join(list(map(str,result[:10])))))