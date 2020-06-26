import sys
from collections import deque


def main():
    que = deque([])
    size = 0
    for n in range(int(input())):
        command = list(sys.stdin.readline().split())
        if command[0] == 'push':
            que.append(int(command[1]))
            size += 1
        elif command[0] == 'pop':
            if que:
                print(que.popleft())
                size -= 1
            else:
                print("-1")
        elif command[0] == 'size':
            print(size)
        elif command[0] == 'empty':
            print(0 if que else 1)
        elif command[0] == 'front':
            if que:
                print(que[0])
            else:
                print(-1)
        elif command[0] == 'back':
            if que:
                print(que[-1])
            else:
                print(-1)


if __name__ == '__main__':
    main()
