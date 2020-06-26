def solve(arg):
    stack = []
    for ch in arg:
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return "no"
        elif ch == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return "no"
    return "no" if stack else "yes"


if __name__ == '__main__':
    sentence = input()
    while sentence != '.':
        print(solve(sentence))
        sentence = input()
