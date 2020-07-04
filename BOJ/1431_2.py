def main():
    numbers = [input() for _ in range(int(input()))]
    numbers.sort(key=lambda x: (len(x), sum([int(i) for i in x if 48 <= ord(i) <= 57]), x))
    for number in numbers:
        print(number)


main()
