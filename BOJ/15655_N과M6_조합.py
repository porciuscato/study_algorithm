import sys
import datetime

sys.stdin = open('15655.txt')

def combi(arr, depth, last):
    if depth == M:
        for num in arr:
            sys.stdout.write(str(num) + ' ')
        sys.stdout.write('\n')
    else:
        for i in range(last, N):
            arr[depth] = NUMBERS[i]
            combi(arr, depth + 1, i + 1)

if __name__ == '__main__':
    start = datetime.datetime.now()
    N, M = map(int, input().split())
    NUMBERS = sorted(list(map(int, input().split())))
    result = [0] * M
    combi(result, 0, 0)
    print((datetime.datetime.now() - start).total_seconds())