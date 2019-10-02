import sys

sys.stdin = open('input.txt', 'r')

def make_combi(arr, depth, last):
    global combi
    if depth == 2:
        combi.append(arr)
    else:
        for i in range(last, length):
            ar = arr[:]
            ar.append(i)
            make_combi(ar, depth + 1, i + 1)


def make_combi_repeat(arr, depth, last):
    global ans
    if depth == su:
        du_pan = pan[:]
        for a in arr:
            du_pan[combi[a][0]], du_pan[combi[a][1]] = du_pan[combi[a][1]], du_pan[combi[a][0]]
        result = int(''.join(list(map(str, du_pan))))
        if result > ans:
            ans = result
    else:
        for i in range(last, len_combi):
            ar = arr[:]
            ar.append(i)
            make_combi_repeat(ar, depth + 1, i)


for T in range(1, int(input()) + 1):
    ans = 0
    pan, su = map(int, input().split())
    pan = list(str(pan))

    # 조합생성
    length = len(pan)
    combi = []
    make_combi([], 0, 0)

    # 중복조합 생성
    len_combi = len(combi)
    make_combi_repeat([], 0, 0)
    print('#{} {}'.format(T, ans))