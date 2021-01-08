from itertools import combinations


def solution(relation):
    col_len = len(relation[0])
    temp_arr = [_ for _ in range(col_len)]
    answers = []

    for i in range(1, col_len + 1):
        for data in combinations(temp_arr, i):
            # 최소성 검증
            mini = True
            for answer in answers:
                if mini:
                    cnt = 0
                    for ans in answer:
                        if ans in data:
                            cnt += 1
                    if cnt == len(answer):
                        mini = False
                        break
            
            # 최소성 만족할 경우
            if mini:
                temp_relation = []
                for tupl in relation:
                    temp_relation.append([tupl[n] for n in data])
                # 유일성 검증
                unique = True
                for i in range(0, len(relation) - 1):
                    if unique:
                        for j in range(i + 1, len(relation)):
                            if temp_relation[i] == temp_relation[j]:
                                unique = False
                                break
                if unique:
                    answers.append(data)
    return len(answers)


cases = [
    [["100", "ryan", "music", "2"],
     ["200", "apeach", "math", "2"],
     ["300", "tube", "computer", "3"],
     ["400", "con", "computer", "4"],
     ["500", "muzi", "music", "3"],
     ["600", "apeach", "music", "2"]]
]

for case in cases:
    print(solution(case))
