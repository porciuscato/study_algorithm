import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))
    trees.sort(reverse=True)

    possibles = []
    left = 0
    right = max(trees)
    while left <= right:
        mid = (left + right) // 2
        result = 0
        for tree in trees:
            if tree > mid:
                result += tree - mid
            else:
                break
        if result >= M:
            possibles.append(mid)
            left = mid + 1
        else:
            right = mid
        if left == right and left == mid:
            break
    print(max(possibles))
