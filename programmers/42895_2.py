calc = ["con", "+", "-", "*", "//"]


def equation(N, arr):
    equa = str(N)
    for mark in arr:
        if mark == "con":
            equa += str(N)
        else:
            equa += mark + str(N)
    return eval(equa)


def solution(N, number):
    def permu_rep(i, arr, depth):
        nonlocal flag
        if depth == i:
            if equation(N, arr) == number:
                flag = True
        else:
            for j in range(5):
                ar = arr[:]
                ar.append(calc[j])
                permu_rep(i, ar, depth + 1)

    for i in range(8):
        flag = False
        permu_rep(i, [], 0)
        if flag:
            return i + 1
    return -1


cases = [
    (5, 12),
    (5, 31168)
]

for case in cases:
    print(solution(*case))
