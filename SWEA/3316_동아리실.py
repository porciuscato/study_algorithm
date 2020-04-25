import sys

sys.stdin = open('3316.txt')

# import re
#
#
# CASES = [
#     'A', 'B', 'C', 'D',
#     'AB', 'AC', 'AD', 'BC', 'BD', 'CD',
#     'ABC', 'ABD', 'ACD', 'BCD',
#     'ABCD',
# ]
#
#
# def solve(arr, depth, size):
#     global visited, answer
#     if depth == 0:
#         p = re.compile('.*' + '.*'.join(list(arr)) + '.*')
#         temp_arr = []
#         for c in CASES:
#             if p.match(c):
#                 temp_arr.append(c)
#         for idx in range(len(temp_arr)):
#             solve(temp_arr[idx], depth + 1, size)
#     elif depth == size:
#         answer += 1
#     else:
#         # 'AB'
#         p = re.compile('.*' + duty[depth] + '.*')
#         temp_arr = []
#         for c in CASES:
#             if p.match(c):
#                 temp_arr.append(c)
#
#         temp_arr2 = []
#         for es in list(arr):
#             pp = re.compile('.*' + es + '.*')
#             for t in temp_arr:
#                 if pp.match(t):
#                     temp_arr2.append(t)
#         temp_arr2 = list(set(temp_arr2))
#         for tt in temp_arr2:
#             solve(tt, depth + 1, size)
#
#
# for T in range(1, int(input()) + 1):
#     visited = [0] * 15  # len(CASES)
#     answer = 0
#     duty = input()
#     SIZE = len(duty)
#     start = 'A' if duty[0] == 'A' else 'A' + duty[0]
#     solve(start, 0, SIZE)
#     print('#{} {}'.format(T, answer % 1000000007))
d = {'A': 3, 'B': 2, 'C': 1, 'D': 0}
mod = 1000000007
for tc in range(int(input())):
    n = input()
    tl = [[] for _ in range(len(n))]
    if n[0] == 'A':
        for j in range(1, 16):
            if j & (1 << 3):
                tl[0].append([j, 1])
    else:
        for j in range(1, 16):
            if j & (1 << 3) and j & (1 << d[n[0]]):
                tl[0].append([j, 1])
    for i in range(1, len(n)):
        tmp = []
        for j in range(1, 16):
            if j & (1 << d[n[i]]):
                tmp.append([j, 0])

        for n1 in tl[i - 1]:
            for n2 in tmp:
                if n1[0] & n2[0]:
                    n2[1] = (n2[1] + n1[1]) % mod
        tl[i] = tmp
    ans = 0
    for x in tl[-1]:
        ans = (x[1] + ans) % mod
    print('#{} {}'.format(tc + 1, ans))