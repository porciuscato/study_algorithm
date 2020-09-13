cluster = [
    ['cpp', 'backend', 'junior', 'chicken', [], 0],
    ['cpp', 'backend', 'junior', 'pizza', [], 0],
    ['cpp', 'backend', 'senior', 'chicken', [], 0],
    ['cpp', 'backend', 'senior', 'pizza', [], 0],
    ['cpp', 'frontend', 'junior', 'chicken', [], 0],
    ['cpp', 'frontend', 'junior', 'pizza', [], 0],
    ['cpp', 'frontend', 'senior', 'chicken', [], 0],
    ['cpp', 'frontend', 'senior', 'pizza', [], 0],
    ['java', 'backend', 'junior', 'chicken', [], 0],
    ['java', 'backend', 'junior', 'pizza', [], 0],
    ['java', 'backend', 'senior', 'chicken', [], 0],
    ['java', 'backend', 'senior', 'pizza', [], 0],
    ['java', 'frontend', 'junior', 'chicken', [], 0],
    ['java', 'frontend', 'junior', 'pizza', [], 0],
    ['java', 'frontend', 'senior', 'chicken', [], 0],
    ['java', 'frontend', 'senior', 'pizza', [], 0],
    ['python', 'backend', 'junior', 'chicken', [], 0],
    ['python', 'backend', 'junior', 'pizza', [], 0],
    ['python', 'backend', 'senior', 'chicken', [], 0],
    ['python', 'backend', 'senior', 'pizza', [], 0],
    ['python', 'frontend', 'junior', 'chicken', [], 0],
    ['python', 'frontend', 'junior', 'pizza', [], 0],
    ['python', 'frontend', 'senior', 'chicken', [], 0],
    ['python', 'frontend', 'senior', 'pizza', [], 0],
]


def binary_search(array, total, point):
    if point <= array[0]:
        return total
    elif point > array[-1]:
        return 0
    else:
        answer = 0
        left = 0
        right = total - 1
        while left <= right:
            if left == right:
                answer = left
                break
            m = (left + right) // 2
            if array[m] == point:
                idx = m
                while array[idx] == point:
                    idx -= 1
                answer = idx + 1
                break
            elif point < array[m]:
                right = m
            elif point > array[m]:
                left = m + 1
        return total - answer


def solution(info, query):
    global cluster
    for person in info:
        result = list((person.split(" ")))
        for tup in cluster:
            if result[:4] == tup[:4]:
                tup[4].append(int(result[4]))
                tup[5] += 1
                break
    for tup in cluster:
        tup[4].sort()

    answer = []
    for condition in query:
        res = [ele for ele in condition.split(' ') if ele != 'and']
        temp = 0
        for tup in cluster:
            if (res[0] == tup[0] or res[0] == '-') and (res[1] == tup[1] or res[1] == '-') and (
                    res[2] == tup[2] or res[2] == '-') and (res[3] == tup[3] or res[3] == '-'):
                point = int(res[4])
                total = tup[5]
                # temp += sum([i >= point for i in tup[4]])
                if total:
                    temp += binary_search(tup[4], total, point)
        answer.append(temp)
    return answer


cases = [
    (["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
      "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
     ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
      "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
      "- and - and - and - 150"])
]

for case in cases:
    print(solution(*case))

# a = [1, 2, 3, 5, 5, 5, 12, 12, 25, 31, 312, 315]
# print(len(a))
# print(binary_search(a, len(a), 4))
