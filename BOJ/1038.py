def main():
    n = int(input())
    size = 10
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    positions = [0, 10]
    idx = 0
    p_idx = 0
    addition = 1
    while size < n:
        start_idx = positions[p_idx]
        for i in range(arr[start_idx:]):
            pass
        if addition == 9:
            addition = 1
            p_idx += 1
            positions.append(size)
    print(arr[n])


main()
