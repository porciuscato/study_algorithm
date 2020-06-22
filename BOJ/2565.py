def main():
    n = int(input())
    array = [[]]
    for _ in range(n):
        array[0].append((tuple(map(int, input().split()))))
    array.append([1] * n)
    array[0].sort(key=lambda x: x[0])
    for idx in range(n):
        val = array[0][idx][1]
        temp = []
        for i in range(idx - 1, -1, -1):
            if val > array[0][i][1]:
                temp.append(array[1][i])
        try:
            array[1][idx] = max(temp) + 1
        except ValueError:
            continue
    print(n - max(array[1]))


main()

