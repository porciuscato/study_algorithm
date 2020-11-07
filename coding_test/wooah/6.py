def solution(logs):
    database = {}
    for log in logs:
        pk, problem, score = log.split()
        if database.get(pk):
            database[pk][problem] = score
        else:
            database[pk] = {problem: score}

    database_2 = {}
    for pk, problems in database.items():
        solved = len(problems)
        if solved >= 5:
            if database_2.get(solved):
                database_2[solved].append(pk)
            else:
                database_2[solved] = [pk]

    answer = []
    for _, arr in database_2.items():
        length = len(arr)
        for i in range(length - 1):
            a = database[arr[i]]
            for j in range(i + 1, length):
                b = database[arr[j]]
                if a == b:
                    answer.append(arr[i])
                    answer.append(arr[j])

    answer = list(set(answer))
    answer.sort()
    return answer if answer else ["None"]


cases = [
    ["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"],
    ["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100",
     "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "2001 1 100",
     "2001 2 100", "2001 4 100", "2001 7 95", "2001 9 100", "2002 1 95", "2002 2 100", "2002 4 100", "2002 7 100",
     "2002 9 100"],
    ["1901 10 50", "1909 10 50"],
    []
]

for case in cases:
    print(solution(case))


