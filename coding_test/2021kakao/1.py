# a: 97 ~ 122
# A: 65 ~ 90
# 0: 48 ~ 57
# -: 45
# _: 95
# .: 46
# print(ord('.'))
# print(chr(97))


def level1(new_id):
    answer = ''
    for char in new_id:
        if 65 <= ord(char) <= 90:
            answer += chr(ord(char) + 32)
        else:
            answer += char
    return answer


def level2(new_id):
    answer = ''
    for char in new_id:
        lett = ord(char)
        if 97 <= lett <= 122 or 65 <= lett <= 90 or 48 <= lett <= 57 or lett == 45 or lett == 95 or lett == 46:
            answer += char
    return answer


def level3(new_id):
    answer = ''
    length = len(new_id)
    idx = 0
    while idx < length:
        c = ord(new_id[idx])
        if c == 46:
            temp = idx + 1
            cnt = 1
            while temp < length and ord(new_id[temp]) == 46:
                cnt += 1
                temp += 1
            if cnt > 1:
                answer += '.'
                idx += cnt
            else:
                answer += '.'
                idx += 1
        else:
            answer += new_id[idx]
            idx += 1
    return answer


def level4(new_id):
    if new_id:
        if new_id[0] == ".":
            new_id = new_id[1:]
    if new_id:
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    return new_id


def level5(new_id):
    if not new_id:
        new_id = "a"
    return new_id


def level6(new_id):
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == ".":
        new_id = new_id[:-1]
    return new_id


def level7(new_id):
    while len(new_id) <= 2:
        new_id += new_id[-1]
    return new_id


def solution(new_id):
    result1 = level1(new_id)
    result2 = level2(result1)
    result3 = level3(result2)
    result4 = level4(result3)
    result5 = level5(result4)
    result6 = level6(result5)
    result7 = level7(result6)
    return result7


cases = [
    "...!@BaT#*..y.abcdefghijklm",
    "",
    "z-+.^.",
    "=.=",
    "123_.def",
    "abcdefghijklmn.p"
]

for case in cases:
    print(solution(case))
