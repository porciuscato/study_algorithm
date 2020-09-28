import sys

input = sys.stdin.readline


if __name__ == "__main__":
    possibles = []
    K, N = map(int, input().split())
    arr = [int(input()) for _ in range(K)]

    left = 1
    right = sum(arr) // N
    while left <= right:
        mid = (left + right) // 2
        result = sum([ele // mid for ele in arr])
        if result >= N:
            possibles.append(mid)
            left = mid + 1
        else:
            right = mid
        if left == right and left == mid:
            break
    if possibles:
        print(max(possibles))
    else:
        print(min(arr))
