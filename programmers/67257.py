operators = (
    ('*', '+', '-'),
    ('*', '-', '+'),
    ('+', '*', '-'),
    ('+', '-', '*'),
    ('-', '*', '+'),
    ('-', '+', '*'),
)


def calculate(que, oper):
    result = []
    flag = False
    calc = ''
    for ele in que:
        if ele == oper:
            flag = True
            calc += result.pop()
            calc += oper
        else:
            if flag:
                calc += ele
                result.append(str(eval(calc)))
                calc = ''
                flag = False
            else:
                result.append(ele)
    return result


def solution(expression):
    que = []
    temp = ''
    for i in range(len(expression)):
        if expression[i].isdigit():
            temp += expression[i]
        else:
            que.append(temp)
            que.append(expression[i])
            temp = ''
    que.append(temp)

    answers = []
    for operator in operators:
        arr = que[:]
        for oper in operator:
            arr = calculate(arr, oper)
        answers.append(abs(int(arr[0])))
    return max(answers)


cases = [
    "100-200*300-500+20",
    "50*6-3*2"
]

for case in cases:
    print(solution(case))

# a = 100
#
# print(type(a) == int)