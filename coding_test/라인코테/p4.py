def solution(snapshots, transactions):
    # 계좌 정보를 받아서 dict로 만든다.
    accounts = {}
    for snapshot in snapshots:
        account, value = snapshot
        accounts[account] = int(value)

    # 모든 트랜잭션을 순서대로 정리하자
    logs = [[0] * 3 for _ in range(10001)]
    for tran in transactions:
        index, action, account, value = tran
        index = int(index)
        row = logs[index]
        if not row[0]:
            row[0] = action
            row[1] = account
            row[2] = int(value)

    # 다 돌면서 계좌를 변동시키자
    for log in logs:
        if log[0]:
            action, account, value = log
            if action == 'SAVE':
                if accounts.get(account):
                    accounts[account] += value
                else:
                    accounts[account] = value
            elif action == 'WITHDRAW':
                accounts[account] -= value

    # print(accounts)
    answer = []
    for account, value in accounts.items():
        answer.append([account, str(value)])

    # 이제 answer를 순서대로 출력
    answer.sort(key=lambda x: x[0])
    return answer


print(solution([["ACCOUNT1", "100"], ["ACCOUNT2", "150"]],
               [["1", "SAVE", "ACCOUNT2", "100"], ["2", "WITHDRAW", "ACCOUNT1", "50"], ["1", "SAVE", "ACCOUNT2", "100"],
                ["4", "SAVE", "ACCOUNT3", "500"], ["3", "WITHDRAW", "ACCOUNT2", "30"]]))
print(solution([
  ["ACCOUNT1", "100"],
  ["ACCOUNT2", "150"],
  ["ACCOUNT10", "150"]
],
    [
        ["1", "SAVE", "ACCOUNT2", "100"],
        ["2", "WITHDRAW", "ACCOUNT1", "50"],
        ["1", "SAVE", "ACCOUNT2", "100"],
        ["4", "SAVE", "ACCOUNT3", "500"],
        ["3", "WITHDRAW", "ACCOUNT2", "30"]
    ]
))