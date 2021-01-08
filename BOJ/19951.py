import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = list(map(int, input().split()))
    array = []
    for _ in range(M):
        a, b, k = map(int, input().split())
        array.append([a - 1, b - 1, k])
    array.sort(key=lambda x: (x[0], x[1]))
    print(' '.join(list(map(str, board))))
