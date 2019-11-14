import sys

sys.stdin = open('4012.txt', 'r')


# def solve(arr):
#     global ans
#     A = [0]
#     B = []
#     for i in range(1, N):
#         if i in arr:
#             A.append(i)
#         else:
#             B.append(i)
#     flavor_A = 0
#     flavor_B = 0
#     for r in range(half):
#         for c in range(half):
#             flavor_A += TABLE[A[r]][A[c]]
#             flavor_B += TABLE[B[r]][B[c]]
#     result = abs(flavor_A - flavor_B)
#     if result < ans:
#         ans = result


def combi(arr, depth, last):
    global ans
    if depth == half - 1:
        A = [0]
        B = []
        for i in range(1, N):
            if i in arr:
                A.append(i)
            else:
                B.append(i)
        flavor_A = 0
        flavor_B = 0
        for r in range(half):
            for c in range(half):
                flavor_A += TABLE[A[r]][A[c]]
                flavor_B += TABLE[B[r]][B[c]]
        result = abs(flavor_A - flavor_B)
        if result < ans:
            ans = result
    else:
        for i in range(last, N):
            ar = arr[:]
            ar.append(i)
            combi(ar, depth + 1, i + 1)


for T in range(1, int(input()) + 1):
    ans = 1e5
    N = int(input())
    TABLE = [list(map(int, input().split())) for _ in range(N)]
    ingredients = [0] * N
    half = N // 2
    # 2개로 나누는 조합
    combi([], 0, 1)
    print('#{} {}'.format(T, ans))
