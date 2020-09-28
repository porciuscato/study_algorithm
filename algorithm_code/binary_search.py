def binary_search(arr, value):
    left = 0
    right = len(arr) - 1
    while left < right:
        m = (left + right) // 2
        if arr[m] == value:
            return True
        if value < arr[m]:
            right = m
        else:
            left = m + 1
    return False


arr = [9, 11, 11, 11, 13, 16, 18, 18, 19, 26, 28, 30, 32, 37, 37, 39, 42, 42, 51, 53, 53, 55, 59, 60, 65, 70, 74, 76, 80, 82, 87, 89, 97]

cases = [11]

for c in cases:
    print(binary_search(arr, c))
