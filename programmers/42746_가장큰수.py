# 흠 퀵소트 한 번 구현해보자

import random


def q_sort(arr: list, left, right):
    if left < right:
        pivot, lp, rp = left, left, right
        while lp < rp:
            while lp < right and arr[lp] >= arr[pivot]:
                lp += 1
            while rp > left and arr[rp] < arr[pivot]:
                rp -= 1
            if lp < rp:
                arr[lp], arr[rp] = arr[rp], arr[lp]
        if arr[pivot] <= arr[rp]:
            arr[rp], arr[pivot] = arr[pivot], arr[rp]
        q_sort(arr, left, rp - 1)
        q_sort(arr, rp + 1, right)


def quicksort(arr: list):
    q_sort(arr, 0, len(arr) - 1)



array = []
SIZE = 10
for _ in range(SIZE):
    array.append(random.randint(1, 100))

quicksort(array)

print(array)
