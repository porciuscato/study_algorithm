for T in range(1,int(input())+1):
    N = input()
    M = input()
    idx = len(N) - 1
    result = 0
    while idx < len(M):
        if N[-1] == M[idx]:
            if N == M[idx + 1- len(N):idx + 1]:
                result = 1
                break
            else:
                idx += 1
        else:
            idx += 1
    print('#{} {}'.format(T,result))
