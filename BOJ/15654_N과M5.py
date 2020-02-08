import sys
import datetime

sys.stdin = open('15654.txt')

def permu(arr, depth):
    global visited, RESULT
    if depth == M:
        if NO:
            for i in range(M):
                sys.stdout.write(str(arr[i]) + ' ')
            sys.stdout.write('\n')
        else:
            if arr in RESULT:
                return
            else:
                RESULT.append(arr)
                for i in range(M):
                    sys.stdout.write(str(arr[i]) + ' ')
                sys.stdout.write('\n')
    else:
        for idx in range(N):
            if not visited[idx]:
                ar = arr[:]
                ar.append(NUMBERS[idx])
                visited[idx] = 1
                permu(ar, depth + 1)
                visited[idx] = 0

if __name__ == '__main__':
    start = datetime.datetime.now()
    N, M = map(int, input().split())
    NUMBERS = sorted(list(map(int, input().split())))
    NO = False
    if N == len(set(NUMBERS)):
        NO = True

    visited = [0] * N
    RESULT = []
    permu([], 0)
    print((datetime.datetime.now() - start).total_seconds())