import sys
from heapq import heappush, heappop


input = sys.stdin.readline


def main():
    global ans
    possibles = []
    arr.sort()
    for m, v in arr:
        if v != 2000000:
            heappush(possibles, -v)
        else:
            if possibles:
                ans += -heappop(possibles)


if __name__ == '__main__':
    N, K = map(int, input().split())
    arr = []
    for n in range(N):
        m, v = map(int, input().split())
        arr.append((m, v))
    for k in range(K):
        arr.append((int(input()), 2000000))
    ans = 0
    main()
    print(ans)
