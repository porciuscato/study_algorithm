N = int(input())
answer = [0, 1, 2]
if N < 2:
    print(answer[N])
else:
    for i in range(3, N + 1):
        value = answer[i - 1] + answer[i - 2]
        answer.append(value % 15746)
    print(answer[N])
