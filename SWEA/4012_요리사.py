import sys

sys.stdin = open('4012.txt', 'r')


def combi(arr, depth, last):
    if depth == half - 1:
        pass
    else:
        for i in range()


for T in range(1, int(input()) + 1):
    ans = 0
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    ingredients = [0] * N
    half = N // 2
    # 2개로 나누는 조합을 구해보자.
    combi([], 0, 0)
    print('#{} {}'.format(T, ans))
