from itertools import combinations


def main():
    arr = [i for i in range(12)]
    size = 0
    for j in combinations(arr, 10):
        size += 1
    print(size)


main()

