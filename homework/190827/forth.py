for T in range(1, int(input()) + 1):
    sentence = input().split()
    stack = []
    for c in sentence:
        if c.isdecimal():
            stack.append(c)
        elif c == '+' or c == '*' or c == '-' or c == '/':
            if len(stack) < 2:
                print('#{} error'.format(T))
                break
            else:
                b = int(stack.pop(-1))
                a = int(stack.pop(-1))
                if c == '+':
                    d = a + b
                    stack.append(d)
                elif c == '*':
                    d = a * b
                    stack.append(d)
                elif c == '-':
                    d = a - b
                    stack.append(d)
                elif c == '/':
                    d = int(a / b)
                    stack.append(d)
        elif c == '.':
            result = stack.pop(-1)
            if stack:
                print('#{} error'.format(T))
            else:
                print('#{} {}'.format(T, result))
                break
