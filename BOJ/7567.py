braces = list(input())
length = len(braces)

answer = 0
if braces:
    answer += 10
for i in range(1, length):
    if braces[i - 1] == braces[i]:
        answer += 5
    else:
        answer += 10

print(answer)