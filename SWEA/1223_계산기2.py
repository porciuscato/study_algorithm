import sys

sys.stdin = open('1223.txt', 'r')

for T in range(1, 11):
    N = int(input())
    inputs = input()
    stack = []
    multiple = 0
    for n in range(N):
        value = inputs[n]
        if multiple:
            popped = stack.pop()
            stack.append(int(value) * popped)
            multiple = 0
        elif value not in ('+', '*'):
            stack.append(int(value))
        elif value == '*':
            multiple = 1
    print(f'#{T} {sum(stack)}')
