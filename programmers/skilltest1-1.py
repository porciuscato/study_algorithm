n = 1234

answer = 0
val = n
rem = 0

while not (val == 0 and rem == 0):
    rem = val % 10
    val = val // 10
    answer += rem

print(answer)