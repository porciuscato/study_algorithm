# 전화번호 목록


def solution(phone_book):
    LEN_DICT = {}
    for i in range(1, 21):
        LEN_DICT[i] = []
    for number in phone_book:
        length = len(number)
        LEN_DICT[length].append(number)
    for start in range(1, 21):
        for value in LEN_DICT[start]:
            for check in range(start, 21):
                if start == check:
                    if len(LEN_DICT[start]) != len(set(LEN_DICT[start])):
                        return False
                else:
                    for target in LEN_DICT[check]:
                        if target[0:start] == value:
                            return False
    else:
        return True


print(solution(["123", "456", "789"]))