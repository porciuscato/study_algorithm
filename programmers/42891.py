def solution(food_times, k):
    database = {}
    for idx in range(1, len(food_times) + 1):
        num = food_times[idx - 1]
        if database.get(num):
            database[num]["cnt"] += 1
            database[num]["list"].append(idx - 1)
        else:
            database[num] = {}
            database[num]["cnt"] = 1
            database[num]["list"] = [idx - 1]
    data = sorted(list(database.keys()))
    print(database)
    print(data)

    food_count = len(food_times)
    total_time = sum(food_times)
    print(total_time)
    answer = 0

    return answer


cases = [
    [[3, 1, 2], 5],
    [[4, 2, 3, 2, 3, 4, 1, 3, 1], 10]
]

for case in cases:
    print(solution(*case))
