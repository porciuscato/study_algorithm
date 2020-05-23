def q_sort(arr, left, right, reverse):
    if left < right:
        pivot, lp, rp = left, left, right
        while lp < rp:
            while lp < right and (arr[lp] <= arr[pivot] if not reverse else arr[lp] >= arr[pivot]):
                lp += 1
            while rp > left and (arr[rp] > arr[pivot] if not reverse else arr[rp] < arr[pivot]):
                rp -= 1
            if lp < rp:
                arr[lp], arr[rp] = arr[rp], arr[lp]
        if arr[rp] <= arr[pivot] if not reverse else arr[rp] >= arr[pivot]:
            arr[rp], arr[pivot] = arr[pivot], arr[rp]
        q_sort(arr, left, rp - 1, reverse)
        q_sort(arr, rp + 1, right, reverse)


def quicksort(arr: list, reverse=False):
    q_sort(arr, 0, len(arr) - 1, reverse)
