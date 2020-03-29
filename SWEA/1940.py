import sys

sys.stdin = open('1940.txt', 'r')

for T in range(1, int(input()) + 1):
    N = int(input())
    answer = 0
    velocity = 0
    for n in range(N):
        inputs = list(map(int, input().split()))
        state = inputs[0]
        if state == 1:
            velocity += inputs[1]
        elif state == 2:
            velocity -= inputs[1]
            if velocity < 0:
                velocity = 0
        answer += velocity
    print('#{} {}'.format(T, answer))
