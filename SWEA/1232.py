import sys

sys.stdin = open('input.txt', 'r')


def postorder(node):
    global stack, ans
    if data[node][1]:
        postorder(data[node][1])
    if data[node][2]:
        postorder(data[node][2])
    if data[node][0].isdecimal():
        stack.append(int(data[node][0]))
    else:
        suf = stack.pop(-1)
        pre = stack.pop(-1)
        if data[node][0] == '+':
            ans = pre + suf
        elif data[node][0] == '-':
            ans = pre - suf
        elif data[node][0] == '*':
            ans = pre * suf
        elif data[node][0] == '/':
            ans = pre / suf
        stack.append(ans)


for T in range(1, 11):
    N = int(input())
    data = [[0] * 3 for _ in range(N + 1)]
    ans = 0
    stack = []
    for _ in range(N):
        d = list(input().split())
        d += [0, 0]
        idx = int(d[0])
        data[idx][0] = d[1]
        data[idx][1] = int(d[2])
        data[idx][2] = int(d[3])
    postorder(1)
    print("#{} {}".format(T, int(ans)))
