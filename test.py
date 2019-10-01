import sys
from datetime import datetime

sys.stdin = open('output.txt', 'r')


def partition(arr, left, right):
    pivot = arr[left]
    lp = left + 1
    rp = right
    while lp < rp:
        while arr[lp] < pivot:
            if lp == N - 1:
                break
            else:
                lp += 1
        while arr[rp] > pivot:
            if rp == 0:
                break
            else:
                rp -= 1
        
    return 0


def quick_sort(arr, left, right):
    if left < right:
        cri = partition(arr, left, right)
        quick_sort(arr, left, cri - 1)
        quick_sort(arr, cri + 1, right)


def qsort(arr):
    quick_sort(arr, 0, N - 1)


start = datetime.now()
for T in range(1, int(input()) + 1):
    N = int(input())
    num = list(map(int, input().split()))
    qsort(num)
    print(num)
    print('#{} {}'.format(T, num[N // 2]))
print(datetime.now() - start)
