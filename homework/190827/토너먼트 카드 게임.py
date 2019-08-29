def match(p1, p2):
    if p1[1] == 1:
        if p2[1] == 1:
            return p1 if p1[0] < p2[0] else p2
        elif p2[1] == 2:
            return p2
        elif p2[1] == 3:
            return p1
    elif p1[1] == 2:
        if p2[1] == 1:
            return p1
        elif p2[1] == 2:
            return p1 if p1[0] < p2[0] else p2
        elif p2[1] == 3:
            return p2
    elif p1[1] == 3:
        if p2[1] == 1:
            return p2
        elif p2[1] == 2:
            return p1
        elif p2[1] == 3:
            return p1 if p1[0] < p2[0] else p2


def tournament(arr, start, end):
    if (end - start) == 1:
        return arr[start]
    else:
        mid = (start + end) // 2
        player1 = tournament(arr, start, mid)
        player2 = tournament(arr, mid, end)
        return match(player1, player2)


for T in range(1, int(input()) + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    students = [i for i in range(1, N + 1)]
    players = list(zip(students, cards))
    victory = tournament(players, 0, N)
    print('#{} {}'.format(T, victory[0]))
