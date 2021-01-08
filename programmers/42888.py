def solution(record):
    answer = []
    db = {}
    for line in record:
        l = line.split()
        if len(l) == 3:
            op, _id, alias = line.split()
            if op == "Enter" or op == "Change":
                db[_id] = alias
    for line in record:
        l = line.split()
        op, _id = l[0], l[1]
        if op == "Enter":
            answer.append(f"{db[_id]}님이 들어왔습니다.")
        elif op == "Leave":
            answer.append(f"{db[_id]}님이 나갔습니다.")
    return answer


cases = [
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
]

for case in cases:
    print(solution(case))
