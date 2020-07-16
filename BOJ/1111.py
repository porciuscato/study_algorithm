def main():
    if N <= 2:
        if N == 2 and numbers[0] == numbers[1]:
            print(numbers[0])
        else:
            print("A")
    else:
        denominator = numbers[1] - numbers[0]
        numerator = numbers[2] - numbers[1]
        if denominator == 0 and numerator == 0:
            a = 1
            b = 0
        elif denominator == 0:
            print("B")
            return
        elif numerator == 0:
            a = 0
            b = numbers[1]
        else:
            a = (numbers[2] - numbers[1]) / (numbers[1] - numbers[0])
            b = numbers[2] - numbers[1] * a

        if a % 1 != 0 or b % 1 != 0:
            print("B")
        else:
            a = int(a)
            b = int(b)
            for i in range(2, N - 1):
                if numbers[i + 1] != numbers[i] * a + b:
                    print("B")
                    return
            print(numbers[-1] * a + b)


if __name__ == "__main__":
    N = int(input())
    numbers = list(map(int, input().split()))
    main()
