import sys

sys.stdin = open('input.txt', 'r')

# 입력을 받는다.
# 변수 2개를 설정한다
# 하나는 고용해야할 사람 수 : 이것이 정답
# 하나는 앞으로 갈 수 있는 수. 이건 가면서 갱신해낸다.
for T in range(1, int(input()) + 1):
    hire = 0
    go = 0
    data = list(map(int, list(input())))
    for d in range(len(data)):
        go += data[d]
        if go == 0:
            hire += 1
            go += 1
        go -= 1
    print("#{} {}".format(T, hire))
