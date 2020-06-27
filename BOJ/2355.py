def subsum(n: int):
    return (n * (n + 1)) // 2


def main():
    A, B = map(int, input().split())
    if A * B > 0:
        if A >= B:
            big = A
            small = B
        else:
            big = B
            small = A
        if big > 0:
            print(subsum(big) - subsum(small - 1))
        else:
            print(-(subsum(abs(small)) - subsum(abs(big) - 1)))
    elif A * B == 0:
        value = A + B
        print(subsum(value) if value >= 0 else -subsum(value))
    else:
        if A > B:
            big = A
            small = B
        else:
            big = B
            small = A
        print(subsum(big) - subsum(abs(small)))


main()
