num = 10
div = 12
d = num % div
l = [d]
print(num, d)
for i in range(1, 15):
    n = d * num
    d = n % div
    l.append(d)
    print(n, n % div)

print(l)
