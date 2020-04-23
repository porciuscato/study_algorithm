a = int(input())
b = int(input())
b_3 = b % 10
b_4 = ((b - b_3) // 10) % 10
b_5 = b // 100
a_3 = a * b_3
a_4 = a * b_4
a_5 = a * b_5
a_6 = a * b
print(a_3)
print(a_4)
print(a_5)
print(a_6)
