def score_sort(node):
    if node.get("arr"):
        node["arr"].sort()
    else:
        for key in node:
            score_sort(node[key])


# binary_search
def count_people(arr, left, right, score):
    if left <= right:
        mid = (left + right) // 2
        if score < arr[mid]:
            if mid - 1 < 0:
                return len(arr) - left
            l_val = arr[mid - 1]
            if l_val < score:
                return len(arr) - mid
            else:
                return count_people(arr, left, mid - 1, score)
        elif score == arr[mid]:
            if mid - 1 < 0:
                return len(arr) - left
            l_val = arr[mid - 1]
            if l_val == score:
                return count_people(arr, left, mid - 1, score)
            else:
                return len(arr) - mid
        else:
            return count_people(arr, mid + 1, right, score)
    else:
        return 0


def find_arr(node, quer, depth):
    tot = 0
    for key in node:
        if node.get("arr"):
            return count_people(node["arr"], 0, len(node["arr"]) - 1, quer[depth])
        else:
            if quer[depth] == key or quer[depth] == '-':
                tot += find_arr(node[key], quer, depth + 1)
    return tot


def solution(info, query):
    answer = []
    # db 구축
    database = {}
    for tup in info:
        row = tup.split(" ")
        row[4] = int(row[4])
        node = database
        for i in range(4):
            if not node.get(row[i]):
                node[row[i]] = {}
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
        answer.append(find_arr(database, quer, 0))
    return answer


cases = [
    (["java backend junior pizza 150",
      "python frontend senior chicken 210",
      "python frontend senior chicken 150",
      "cpp backend senior pizza 260",
      "java backend junior chicken 80",
      "python backend senior chicken 50"],
     ["java and backend and junior and pizza 100",
      "python and frontend and senior and chicken 200",
      "cpp and - and senior and pizza 250",
      "- and backend and senior and - 150",
      "- and - and - and chicken 100",
      "- and - and - and - 150"]),
]

for case in cases:
    print(solution(*case))
