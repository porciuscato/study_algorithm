def quick_sort(arr, left, right):
    if left < right:
        pivot = left
        lp = left
        rp = right
        while lp < rp:
            while lp < right and arr[lp] <= arr[pivot]:
                lp += 1
            while rp > 0 and arr[rp] > arr[pivot]:
                rp -= 1
            if lp < rp:
                arr[lp], arr[rp] = arr[rp], arr[lp]
        if arr[pivot] >= arr[rp]:
            arr[rp], arr[pivot] = arr[pivot], arr[rp]
        p = rp
        quick_sort(arr, left, p - 1)
        quick_sort(arr, p + 1, right)


def q_sort(arr):
    quick_sort(arr, 0, len(arr) - 1)


for T in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    q_sort(arr)
    print('#{} {}'.format(T, arr[N // 2]))