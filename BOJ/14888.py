import sys

sys.stdin = open('14888.txt')


def brute_force(result, depth, operand):
    global OPERAND, mx, mn
    if depth == NUM:
        mx = max(mx, result)
        mn = min(mn, result)
    else:
        oper = operand[::]
        next_num = NUMBERS[depth]
        if oper[0]: # +
            oper[0] -= 1
            brute_force(result + next_num, depth + 1, oper)
            oper[0] += 1
        if oper[1]: # -
            oper[1] -= 1
            brute_force(result - next_num, depth + 1, oper)
            oper[1] += 1
        if oper[2]: # * 
            oper[2] -= 1
            brute_force(result * next_num, depth + 1, oper)
            oper[2] += 1
        if oper[3]: # /
            oper[3] -= 1
            if result < 0:
                result *= -1
                brute_force((result // next_num) * -1, depth + 1, oper)
            else:
                brute_force(result // next_num, depth + 1, oper)
            oper[3] += 1

NUM = int(input())
NUMBERS = list(map(int, (input().split())))
OPERAND = list(map(int, (input().split())))
mx = -10e9
mn = 10e9

brute_force(NUMBERS[0], 1, OPERAND)

print(mx)
print(mn)