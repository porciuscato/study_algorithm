def main():
    for t in range(int(input())):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        a = (x2 - x1) * 2
        b = (y2 - y1) * 2
        c = (r2 ** 2 - x2 ** 2 - y2 ** 2) - (r1 ** 2 - x1 ** 2 - y1 ** 2)
        if a == 0 and b == 0:
            print(-1 if c == 0 else 0)
            continue
        d = abs(a * x1 + b * y1 + c) / ((a ** 2 + b ** 2) ** 0.5)
        if d > r1:
            print(0)
        elif d == r1:
            print(1)
        else:
            print(2)


main()
