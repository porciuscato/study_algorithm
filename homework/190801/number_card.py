# 4834
for T in range(1, int(input()) + 1):
    N = int(input())
    ai = list(map(int, [ch for ch in input()]))
    counting = [0 for i in range(10)]
    for idx in ai:
        counting[idx] += 1
    high_idx = 0
    high_value = counting[high_idx]
    for i in range(1, 10):
        if high_value <= counting[i]:
            high_value = counting[i]
            high_idx = i
    print('#{} {} {}'.format(T, high_idx, high_value))
