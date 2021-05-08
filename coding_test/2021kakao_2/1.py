alphabets = ['zero', 'one', 'two', 'three', 'four',
             'five', 'six', 'seven', 'eight', 'nine']


def solution(s):
    answer = ''
    temp = ''
    start = -1
    end = 0
    while end < len(s):
        if s[end].isdigit():
            answer += s[end]
            end += 1
        else:
            if start == -1:
                start = end
            temp += s[end]
            if len(temp) == 3:
                for i in range(10):
                    word = alphabets[i]
                    if temp in word:
                        end = start + len(word)
                        start = -1
                        answer += str(i)
                        temp = ''
                        break
            else:
                end += 1
    return int(answer)


cases = [
    "one4seveneight",
    "23four5six7",
    "2three45sixseven",
    "123"
]

for case in cases:
    print(solution(case))
