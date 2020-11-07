def solution(money, expected, actual):
    bet = 100
    for i in range(len(expected)):
        temp_money = money - bet
        if temp_money >= 0:
            money = temp_money
        else:
            bet = money
            money = 0
        if expected[i] == actual[i]:
            money += bet * 2
            bet = 100
        else:
            bet *= 2
        if money <= 0:
            money = 0
            break
    return money


cases = [
    (1000, ["H", "T", "H", "T", "H", "T", "H"], ["T", "T", "H", "H", "T", "T", "H"]),
    (1200, ["T", "T", "H", "H", "H"], ["H", "H", "T", "H", "T"]),
    (1500, ["H", "H", "H", "T", "H"], ["T", "T", "T", "H", "T"]),
]

for case in cases:
    print(solution(*case))
