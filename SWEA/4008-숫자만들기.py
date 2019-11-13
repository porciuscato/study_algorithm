# 순열의 중복을 줄이는 법?

import sys

sys.stdin = open('4008.txt', 'r')


# # arr는 연산자들의 id를 담고 있다.
# def solve(arr):
#     global mx, mn
#     # 연산할 숫자들의 리스트
#     array = NUMS[:]
#     for i in range(N - 1):
#         operator = arr[i]
#         if operator == 0:  # +
#             array[i + 1] = array[i] + array[i + 1]
#         elif operator == 1:  # -
#             array[i + 1] = array[i] - array[i + 1]
#         elif operator == 2:  # *
#             array[i + 1] = array[i] * array[i + 1]
#         elif operator == 3:  # /
#             array[i + 1] = int(array[i] / array[i + 1])
#     result = array[N - 1]
#     if result < mn:
#         mn = result
#     if result > mx:
#         mx = result
#
#
# def permu(arr, unit):
#     global memo
#     if unit == N - 1:
#         solve(arr)
#     else:
#         for i in range(N - 1):
#             if not visited[i]:
#                 ar = arr[:]
#                 ar.append(OPR[i])
#                 if memo.get(unit + 1) is None:
#                     memo[unit + 1] = []
#                 if ar not in memo[unit + 1]:
#                     memo[unit + 1].append(ar)
#                     visited[i] = 1
#                     permu(ar, unit + 1)
#                     visited[i] = 0
#
#
# for T in range(1, int(input()) + 1):
#     mx = -1e10
#     mn = 1e10
#     N = int(input())
#     opr_input = list(map(int, input().split()))
#     NUMS = list(map(int, input().split()))
#     # 연산자들은 순서대로 0, 1, 2, 3
#     # 각 연산자들을 사용된 횟수만큼 OPR 리스트에 저장한다.
#     OPR = []
#     for e in range(len(opr_input)):
#         for op in range(opr_input[e]):
#             OPR.append(e)
#     # 연산자들로 순열을 구한다.
#     visited = [0] * (N - 1)
#     # 메모이제이션
#     memo = {}
#     permu([], 0)
#     print('#{} {}'.format(T, mx - mn))

# def calc(depth, value, idx):
#     var = NUMS[depth + 1]
#     ope = OPR[idx]
#     if ope == 0:
#         return value + var
#     elif ope == 1:
#         return value - var
#     elif ope == 2:
#         return value * var
#     elif ope == 3:
#         return value // var
#
#
# def solve(depth, value):
#     global mx, mn
#     if depth == N - 1:
#         if value > mx:
#             mx = value
#         if value < mn:
#             mn = value
#         return
#     for i in range(N - 1):
#         val = calc(depth, value, i)
#         visited[i] = 1
#         solve(depth + 1, val)
#         visited[0] = 0
#
#
# for T in range(1, int(input()) + 1):
#     mx = -1e10
#     mn = 1e10
#     N = int(input())
#     opr_input = list(map(int, input().split()))
#     NUMS = list(map(int, input().split()))
#     # 연산자들은 순서대로 0, 1, 2, 3
#     # 각 연산자들을 사용된 횟수만큼 OPR 리스트에 저장한다.
#     OPR = []
#     for e in range(len(opr_input)):
#         for op in range(opr_input[e]):
#             OPR.append(e)
#     visited = [0] * (N - 1)
#     solve(0, NUMS[0])
#     print('#{} {}'.format(T, mx - mn))


# def solve(ope, nums, val):
#     if nums:
#         if ope[0] > 0:
#             solve([ope[0] - 1] + ope[1:], nums[1:], val + nums[0])
#         if ope[1] > 0:
#             solve([ope[0]] + [ope[1] - 1] + ope[2:], nums[1:], val - nums[0])
#         if ope[2] > 0:
#             solve(ope[:2] + [ope[2] - 1] + [ope[3]], nums[1:], val * nums[0])
#         if ope[3] > 0:
#             solve(ope[:3] + [ope[3] - 1], nums[1:], int(val / nums[0]))
#     else:
#         global res
#         res += [val]
#
#
# for T in range(int(input())):
#     input()
#     OPR = list(map(int, input().split()))
#     NUMS = list(map(int, input().split()))
#     res = []
#     solve(OPR, NUMS[1:], NUMS[0])
#     print("#%d" % (T + 1), max(res) - min(res))

def solve(opr, nums, val):
    global mx, mn
    if nums:
        if opr[0] > 0:
            solve([opr[0] - 1] + opr[1:], nums[1:], val + nums[0])
        if opr[1] > 0:
            solve([opr[0]] + [opr[1] - 1] + opr[2:], nums[1:], val - nums[0])
        if opr[2] > 0:
            solve(opr[:2] + [opr[2] - 1] + [opr[3]], nums[1:], val * nums[0])
        if opr[3] > 0:
            solve(opr[:3] + [opr[3] - 1], nums[1:], int(val / nums[0]))
    else:
        if val > mx:
            mx = val
        if val < mn:
            mn = val


for T in range(1, int(input()) + 1):
    mx = -1e10
    mn = 1e10
    N = int(input())
    OPR = list(map(int, input().split()))
    NUMS = list(map(int, input().split()))
    solve(OPR, NUMS[1:], NUMS[0])
    print('#{} {}'.format(T, mx - mn))
