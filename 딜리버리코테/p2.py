OVERFLOW = 1048576
UNDERFLOW = 0


def solution(S):
    stack = []
    size = 0
    for s in S.split(' '):
        if s.isdecimal():
            stack.append(int(s))
            size += 1
        elif s == 'POP':
            if size == 0:
                return -1
            stack.pop(-1)
            size -= 1
        elif s == 'DUP':
            if size == 0:
                return -1
            stack.append(stack[-1])
            size += 1
        elif s == '+':
            if size <= 1:
                return -1
            result = stack.pop(-1) + stack.pop(-1)
            if result >= OVERFLOW:
                return -1
            stack.append(result)
            size -= 1
        elif s == '-':
            if size <= 1:
                return -1
            result = stack.pop(-1) - stack.pop(-1)
            if result < UNDERFLOW:
                return -1
            stack.append(result)
            size -= 1
    return stack[-1] if size != 0 else -1


examples = [
    '13 DUP 4 POP 5 DUP + DUP + -',
    '5 6 + -',
    '3 DUP 5 - -'
]

for ele in examples:
    print(solution(ele))