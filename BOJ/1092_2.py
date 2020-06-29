import sys

input = sys.stdin.readline


def main():
    # import random
    # N = 50
    # crains = [random.randint(1, 1000000) for _ in range(N)]
    # M = 10000
    # boxes = [random.randint(800000, 900000) for _ in range(M)]

    N = int(input())
    crains = list(map(int, input().split()))
    M = int(input())
    boxes = list(map(int, input().split()))
    crains.sort(reverse=True)
    boxes.sort(reverse=True)
    if crains[0] < boxes[0]:
        print(-1)
        return

    positions = [1000000] * N
    for n in range(N):
        v = crains[n]
        for b in range(M):
            if v >= boxes[b]:
                positions[n] = b
                break

    check = [False for _ in range(M)]
    left = M
    ans = 0
    while left != 0:
        for c in range(N):
            for i in range(positions[c], M):
                if not check[i] and crains[c] >= boxes[i]:
                    check[i] = True
                    positions[c] = i
                    left -= 1
                    break
        ans += 1
    print(ans)


main()