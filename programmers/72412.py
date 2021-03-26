def solution(info, query):
    answer = []
    # db 구축
    database = []
    for tup in info:
        database.append(tup.split(" "))
    # 정렬
    database.sort()
    # qeury
    for ask in query:
        ans = 0
        temp = ask.split(" ")
        quer = [temp[0], temp[2], temp[4], temp[6], int(temp[7])]
        for data in database:
            for i in range(5):
                if i < 4:
                    if not (quer[i] == '-' or quer[i] == data[i]):
                        break
                else:
                    if quer[i] > int(data[i]):
                        break
            else:
                ans += 1
        answer.append(ans)
    return answer


cases = [
    (["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]),
]

for case in cases:
    print(solution(*case))
