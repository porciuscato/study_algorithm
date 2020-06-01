def solution(brown, yellow):
    total = brown + yellow
    for ver in range(int(total ** 0.5), 2, -1):
        if total % ver == 0:
            hor = total // ver
            if hor * ver == total:
                for i in range(hor - 2, 0, -1):
                    if yellow % i == 0:
                        j = yellow // i
                        if j <= ver - 2:
                            return [hor, ver]


problems = [
    (10, 2),
    (8, 1),
    (24, 24),
    (5000, 1500000),
    (12, 6),
    (1056, 1024),
    (81344, 1000000)
]

for ele in problems:
    print(solution(*ele))


# def solution(brown, yellow):
#     total = brown + yellow
#     for ver in range(int(total ** 0.5), 2, -1):
#         if total % ver == 0:
#             hor = total // ver
#             if hor * ver == total:
#                 for i in range(hor - 2, 0, -1):
#                     j = yellow // i
#                     if yellow % j == 0 and j <= ver - 2:
#                         return [hor, ver]




# def solution(brown, yellow):
#     total = brown + yellow
#     root = total ** 0.5
#     ver = int(root)
#     hor = total // ver
#     if (root % 1) != 0:
#         result = total % ver
#         while result != 0 or not ((ver - 2 + hor) * 2 <= brown):
#             ver -= 1
#             result = total % ver
#         return [total // ver, ver]
#     else:
#         return [ver] * 2
