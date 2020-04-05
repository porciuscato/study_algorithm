def solution(inputString):
    # 문자열이 들어오면 stack에 넣고 빼는 걸 해야지
    # ( ), { }, [ ], < >
    answer = 0
    stack = []
    # 문자열 돌면서 넣어
    for s in inputString:
        if s == '(':
            stack.append('(')
        elif s == ')':
            try:
                last = stack[-1]
            except:
                return -1
            if last == '(':
                stack.pop()
                answer += 1
            else:
                return -1
        elif s == '{':
            stack.append('{')
        elif s == '}':
            try:
                last = stack[-1]
            except:
                return -1
            if last == '{':
                stack.pop()
                answer += 1
            else:
                return -1
        elif s == '[':
            stack.append('[')
        elif s == ']':
            try:
                last = stack[-1]
            except:
                return -1
            if last == '[':
                stack.pop()
                answer += 1
            else:
                return -1
        elif s == '<':
            stack.append('<')
        elif s == '>':
            try:
                last = stack[-1]
            except:
                return -1
            if last == '<':
                stack.pop()
                answer += 1
            else:
                return -1
    return answer


# print(solution("Hello, world!"))
print(solution("line [plus]"))
# print(solution("if (Count of eggs is 4.) {Buy milk.}"))
