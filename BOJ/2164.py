from collections import deque
import sys


def main():
    N = int(sys.stdin.readline())
    size = N
    array = deque([i for i in range(1, N + 1)])
    while size != 1:
        array.popleft()
        size -= 1
        array.append(array.popleft())
    sys.stdout.write("{}\n".format(array[0]))


if __name__ == "__main__":
    main()
