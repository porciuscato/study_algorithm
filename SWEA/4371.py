import sys

sys.stdin = open('input.txt', 'r')

for T in range(1, int(input()) + 1):
    N = int(input())
    days = [int(input()) for _ in range(N)]
    ships = []
    for d in days[1:]:
        if not ships:
            ships.append(d - 1)
        else:
            for ship in ships:
                if (d - 1) % ship == 0:
                    break
            else:
                ships.append(d - 1)
    print('#{} {}'.format(T, len(ships)))

# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     li = []
#     for i in range(N):
#         li.append(int(input()))
#     mul = []
#     for i in li[1:]:
#         if mul == []:
#             mul.append(i - 1)
#         else:
#             for j in mul:
#                 if (i - 1) % j == 0:
#                     break
#             else:
#                 mul.append(i - 1)
#
#     print('#{0} {1}'.format(tc, len(mul)))