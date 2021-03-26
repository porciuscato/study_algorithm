def score_sort(node):
    if node.get("arr"):
        node["arr"].sort()
    else:
        if node.get("count"):
            for key in node:
                if key != "count":
                    score_sort(node[key])


def count_people(database, quer, depth):

    pass


def solution(info, query):
    answer = []
    # db 구축
    database = {"count": 3}
    for tup in info:
        row = tup.split(" ")
        row[4] = int(row[4])
        node = database
        for i in range(4):
            if not node.get(row[i]):
                node[row[i]] = {"count": 1}
            else:
                node[row[i]]["count"] += 1
            node = node[row[i]]
        if node.get("arr"):
            node["arr"].append(row[4])
        else:
            node["arr"] = [row[4]]

    # 정렬
    score_sort(database)
    # query
    for ask in query:
        temp = ask.split(" ")
        quer = [temp[0], temp[2], temp[4], temp[6], int(temp[7])]
        answer.append(count_people(database, quer, 0))
    return answer


cases = [
    (["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]),
]

for case in cases:
    print(solution(*case))
