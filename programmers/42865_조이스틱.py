from collections import deque


alphabets = dict()
for i in range(65, 91):
    if i >= 78:
        alphabets[chr(i)] = i - 26
    else:
        alphabets[chr(i)] = i


def solution(name):
    name = deque(list(name))
    right_version = name.copy()
    left_version = name.copy()
    left_version.reverse()
    left_version.appendleft(left_version.pop())

    result = []
    for w in (right_version, left_version):
        word = w.copy()
        for i in range(len(name) - 1, -1, -1):
            if w[i] == 'A':
                word.pop()
            else:
                break
        result.append(word)

    task = min(result, key=lambda x: len(x))

    answer = 0
    length = len(task)
    for idx in range(length):
        if idx != 0:
            answer += 1
        answer += abs(65 - alphabets[task[idx]])
    return answer

problems = [
    "JEROEN",
    "JAN",
    "AAAA",  # 0이 나와야 함
    "JJAJAAAAAAAAAJ",
    "AJAJAA",
    "ABAAAA"
]

for pro in problems:
    print(solution(pro))

