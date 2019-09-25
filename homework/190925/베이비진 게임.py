def val(arr):
    for i in range(len(arr) - 2):
        if arr[i] == arr[i + 1] and arr[i + 1] == arr[i + 2]:
            return True
    arr = sorted(list(set(arr)))
    for i in range(len(arr) - 2):
        if arr[i] + 1 == arr[i + 1] and arr[i + 1] + 1 == arr[i + 2]:
            return True
    return False


for T in range(1, int(input()) + 1):
    cards = list(map(int, input().split()))
    p1 = []
    p2 = []
    ans = 0
    for c in range(12):
        if c % 2 == 0:
            p1 += [cards[c]]
        else:
            p2 += [cards[c]]
        if c >= 5 and c % 2:
            p1 = sorted(p1)
            p2 = sorted(p2)
            if val(p1):
                ans = 1
                break
            if val(p2):
                ans = 2
                break
    print('#{} {}'.format(T, ans))
