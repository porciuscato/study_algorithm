def solution(s, op):
    answer = []
    for i in range(1, len(s)):
        l = str(int(s[:i]))
        r = str(int(s[i:]))
        answer.append(eval(l + op + r))
    return answer


cases = [
    ("1234", "+"),
    ("987987", "-"),
    ("31402", "*"),
]

for case in cases:
    print(solution(*case))
