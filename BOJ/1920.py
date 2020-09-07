import sys

inp = sys.stdin.readline


def find(number, left, right):
    while left <= right:
        m = (left + right) // 2
        if number > numbers[m]:
            left = m + 1
        elif number < numbers[m]:
            right = m - 1
        else:
            return 1
    return 0


if __name__ == '__main__':
    N = int(inp())
    numbers = list(map(int, inp().split()))
    M = int(inp())
    finds = list(map(int, inp().split()))
    numbers.sort()
    for num in finds:
        print(find(num, 0, N - 1))
