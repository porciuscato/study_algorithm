from math import ceil


def main():
    global x
    if x == 0:
        print(0)
    else:
        result = []
        if b > 0:
            tx = abs(x)
            while tx != 0:
                result.append(str(tx % b))
                tx = tx // b
            if x < 0:
                result.append("-")
        else:
            while x != 0:
                quo = ceil(x / b)
                result.append(str(x - quo * b))
                x = quo
        print("".join(result[::-1]))


if __name__ == '__main__':
    x, b = map(int, input().split())
    main()
