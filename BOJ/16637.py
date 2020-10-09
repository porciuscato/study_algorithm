import sys
from itertools import combinations


def braces(array):
    res = []
    cal = False
    for i in range(N):
        if i % 2:
            if i in array:
                cal = True
            res.append(exp[i])
        else:
            if cal:
                sym = res.pop()
                num = res.pop()
                if sym == '+':
                    res.append(num + exp[i])
                elif sym == '-':
                    res.append(num - exp[i])
                elif sym == '*':
                    res.append(num * exp[i])
                cal = False
            else:
                res.append(exp[i])
    return res


def calculate(array):
    global ans
    val = array[0]
    cal = None
    for i in range(1, len(array)):
        if i % 2 == 0:
            if cal == '+':
                val += array[i]
            elif cal == '-':
                val -= array[i]
            elif cal == '*':
                val *= array[i]
        else:
            cal = array[i]
    ans = max(ans, val)


def is_fine(array):
    for i in range(len(array) - 1):
        if array[i + 1] - array[i] < 4:
            return False
    return True


if __name__ == "__main__":
    N = int(input())
    in_exp = sys.stdin.readline()
    exp = []
    oper = []
    for i in range(N):
        if i % 2 == 0:
            exp.append(int(in_exp[i]))
        else:
            exp.append(in_exp[i])
            oper.append(i)
    ans = -10000000000
    for i in range((N // 2) + 1):   
        for com in combinations(oper, i):
            if is_fine(com):
                calculate(braces(com))
    print(ans)
