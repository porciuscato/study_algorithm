import sys

sys.stdin = open('1233.txt', 'r')


for T in range(1, 11):
    answer = 1
    N = int(input())
    for n in range(N):
        inputs = input().split()
        if len(inputs) == 2:
            if inputs[1] in ('+', '-', '*', '/'):
                answer = 0
    print(f'#{T} {answer}')