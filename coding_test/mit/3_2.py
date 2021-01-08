def solution(cookies, k):
    length = len(cookies)
    data = [[] for _ in range(length)]
    less_than = [[] for _ in range(length)]
    for i in range(length):
        temp = []
        for j in range(i - 1, -1, -1):
            if cookies[i] > cookies[j]:
                temp.append(j)
        less_than[i] = temp

    for i in range(length):
        present_cookie = cookies[i]
        mx_cnt = 0
        find = False
        for j in less_than[i]:
            experi_cookie = cookies[j]
            if present_cookie > experi_cookie:
                for idx in range(len(data[j])):
                    cnt = data[j][idx][0] + 1
                    if cnt >= mx_cnt:
                        find = True
                        mx_cnt = cnt
                        n_arr = data[j][idx][1][:]
                        n_arr.append(cookies[i])
                        data[i].append((cnt, n_arr))
                    else:
                        break
        if not find:
            data[i].append((1, [cookies[i]]))
        data[i].sort(key=lambda x: -x[0])

    mx = 0
    for line in range(length - 1, -1, -1):
        for ele in data[line]:
            if mx < ele[0]:
                mx = ele[0]
            else:
                break

    cases = []
    for i in range(length - 1, -1, -1):
        for idx in range(len(data[i])):
            if data[i][idx][0] == mx:
                cases.append(data[i][idx][1])
            else:
                break

    cases.sort()
    print(len(cases))
    print(cases)
    return cases[k - 1]


import random

check = [False for i in range(1, 100001)]
t_arr = []
for i in range(500):
    n = random.randint(1, 10000)
    while True:
        if not check[n]:
            check[n] = True
            t_arr.append(n)
            break
        else:
            n = random.randint(1, 10000)


test_arr = [97, 8044, 9966, 4069, 2130, 7559, 8004, 3327, 1455, 4846, 4591, 2503, 2444, 1538, 8016, 8521, 9182, 6868,
            3928, 7386, 2821, 8046, 8684, 2125, 2501, 4462, 3886, 4401, 4034, 7435, 2870, 4706, 4794, 197, 7414, 3680,
            3131, 5181, 6353, 8474, 5939, 4864, 712, 2452, 7484, 1466, 3108, 1216, 4829, 1940, 7608, 4058, 9051, 4773,
            1185, 9710, 7620, 5836, 4705, 5163, 2145, 3719, 8059, 8590, 4568, 6918, 8368, 9864, 1135, 3727, 5510, 6507,
            5031, 575, 6815, 5228, 553, 8635, 5004, 1176, 9362, 201, 5798, 4233, 6539, 9347, 3541, 3583, 2546, 6252,
            4309, 3554, 407, 7192, 3127, 2463, 1295, 8090, 2177, 8970]
tests = [
    # ([1, 4, 2, 6, 5, 3, 7, 15, 9, 8, 12], 2),
    # ([9, 8, 7, 6, 5, 4, 3, 2, 1], 4),
    # ([1], 1)
    # (test_arr, 3),
    # ([i for i in range(100, 0, -1)], 5)
    # (t_arr, 1),
    # ([], 1),
    # ([1, 3750, 2500, 1250, 5000, 8750, 7500, 6250, 10000], 1),
    # ([1, 4, 2, 6, 5, 3, 8, 7], 1),
]

for test in tests:
    # pass
    print(solution(*test))


