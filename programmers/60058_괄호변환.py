def is_right(p):
    stack = []
    for w in p:
        if w == "(":
            stack.append(w)
        elif w == ")":
            if stack:
                if stack[-1] == "(":
                    stack.pop()
                elif stack[-1] == ")":
                    return False
            else:
                return False
    return True if not stack else False


def is_balanced(p):
    left, right = 0, 0
    for w in p:
        if w == "(":
            left += 1
        elif w == ")":
            right += 1
    return True if left == right else False


def divide(p):
    left, right = 0, 0
    for w in p:
        if w == "(":
            left += 1
        elif w == ")":
            right += 1
        if left == right:
            return p[:left + right], p[left + right:]


def u_process(u):
    reverse = ""
    for i in range(1, len(u) - 1):
        if u[i] == "(":
            reverse += ")"
        elif u[i] == ")":
            reverse += "("
    return reverse


def solution(p):
    if is_right(p):
        return p
    else:
        u, v = divide(p)
        answer = ''
        if is_right(u):
            answer += u
            if v:
                answer += solution(v)
        else:
            answer += "(" + solution(v) + ")" + u_process(u)
        return answer


test_cases = [
    "(()())()",
    ")(",
    "()))((()"
]

for case in test_cases:
    print(solution(case))
