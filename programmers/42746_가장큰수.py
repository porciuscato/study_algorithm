def is_greater(num1, num2):
    num1, num2 = str(num1), str(num2)
    if int(num1 + num2) >= int(num2 + num1):
        return True
    else:
        return False


def q_sort(arr: list, left, right):
    if left < right:
        pivot, lp, rp = left, left, right
        while lp < rp:
            while lp < right and is_greater(arr[lp], arr[pivot]):
                lp += 1
            while rp > left and not is_greater(arr[rp], arr[pivot]):
                rp -= 1
            if lp < rp:
                arr[lp], arr[rp] = arr[rp], arr[lp]
        if is_greater(arr[rp], arr[pivot]):
            arr[pivot], arr[rp] = arr[rp], arr[pivot]
        q_sort(arr, left, rp - 1)
        q_sort(arr, rp + 1, right)


def quicksort(arr: list):
    q_sort(arr, 0, len(arr) - 1)


def solution(numbers):
    quicksort(numbers)
    answer = ''.join(list(map(str, numbers)))
    return answer if int(answer) else '0'


problems = [
    [0, 0, 0, 0, 0],
    [40, 403],
    [40, 405],
    [40, 404],
    [12, 121],
    [2, 22, 223],
    [21, 212],
    [41, 415],
    [2, 22],
    [70, 0, 0, 0],
    [0, 0, 0, 1000],
    [12, 1213],
    [0, 0, 1000, 0, 0],
    [0, 1000, 0, 0],
    [121, 12]
]

for problem in problems:
    print(solution(problem))
