import sys

sys.stdin = open('15656.txt')


def dul_permu(depth, last):
    global ARRAY
    if depth == M:
        sys.stdout.write(' '.join(list(map(str, ARRAY))) + '\n')
    else:
        for i in range(last, N):
            ARRAY[depth] = NUMBERS[i]
            dul_permu(depth + 1, i)


if __name__ == '__main__':
    N, M = map(int, input().split())
    NUMBERS = sorted(list(map(int, input().split())))
    ARRAY = [0] * M
    dul_permu(0, 0)