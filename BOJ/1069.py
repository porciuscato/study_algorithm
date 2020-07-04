def main():
    x, y, d, t = map(int, input().split())
    distance = (x ** 2 + y ** 2) ** 0.5
    if t >= d:
        print(distance)
    else:
        quotient = distance // d
        remnant = distance % d
        if remnant == 0:
            print(quotient * t)
        else:
            answers = [quotient * t + (distance - quotient * d), (quotient + 1) * t + ((quotient + 1) * d - distance)]
            print(min(answers))


main()
