for T in range(1, int(input()) + 1):
    tc = input()
    stack = []
    result = 0
    for i in tc:
        if i == '(' or i =='{':
            stack.append(i)
        elif i == ')':
            if not len(stack):
                break
            elif stack[-1] == '(':
                stack.pop(-1)
            else: break
        elif i == '}':
            if not len(stack):
                break
            if stack[-1] == '{':
                stack.pop(-1)
            else: break
    else:
        if not len(stack):
            result = 1
    print('#{} {}'.format(T, result))
