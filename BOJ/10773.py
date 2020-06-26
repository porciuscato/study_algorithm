import sys
input = sys.stdin.readline


def main():
    k = int(input())
    stack = []
    for i in range(k):
        v = int(input())
        if v == 0:
            stack.pop()
        else:
            stack.append(v)
    print(sum(stack))


if __name__ == '__main__':
    main()
