def main():
    while True:
        left, right = map(int, input().split())
        if left == 0 and right == 0:
            break
        if left < right:
            if right % left == 0:
                print("factor")
            else:
                print("neither")
        elif left > right:
            if left % right == 0:
                print("multiple")
            else:
                print("neither")


main()
