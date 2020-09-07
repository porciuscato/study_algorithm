import sys

input2 = sys.stdin.readline
print2 = sys.stdout.write


def find_end(num, left, right, direc):
    if direc == 0:
        ans = N + 1
    else:
        ans = -1
    while left <= right:
        mid = (left + right) // 2
        if num < cards[mid]:
            right = mid - 1
        elif num > cards[mid]:
            left = mid + 1
        else:
            if direc == 0:
                ans = min(ans, mid)
                right = mid - 1
            else:
                ans = max(ans, mid)
                left = mid + 1
    return ans


if __name__ == '__main__':
    N = int(input2())
    cards = list(map(int, input2().split()))
    M = int(input2())
    ms = list(map(int, input2().split()))
    cards.sort()
    for m in ms:
        start = find_end(m, 0, N - 1, 0)
        end = find_end(m, 0, N - 1, 1)
        if start == N + 1:
            print2("0 ")
        else:
            print2("{} ".format(end - start + 1))
