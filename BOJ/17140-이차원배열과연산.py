import sys
from time import sleep

sys.stdin = open('17140_input.txt', 'r')


def solve(d, num):
    global G, mx_row, mx_col
    if d:
        counting = [0] * 101
        traversal = 1
        for cc in range(1, 101):
            if not G[num][cc]:
                continue
            else:
                temp = G[num][cc]
                counting[temp] += 1
                value = counting[temp]
                if value > traversal:
                    traversal = value
            # 행에 대해
        # 그러면 traversal이 확정되겠지
        array = []
        temp_col = 0
        # counting를 쭉 돌면서 0이 나오면 패스하고 값이 타당하면 넣어야지
        tra = 1
        ele = 1
        while tra <= traversal:
            if counting[ele] == tra:
                array.append(ele)
                array.append(tra)
                temp_col += 2
                if temp_col == 100:
                    break
            if ele < 100:
                ele += 1
            else:
                tra += 1
                ele = 1
        # 이러면 array가 확정돼지!
        # 다시 넣어
        if temp_col > mx_col:
            mx_col = temp_col
        for ccc in range(1, temp_col + 1):
            G[num][ccc] = array[ccc - 1]
        for ccc in range(temp_col + 1, 101):
            G[num][ccc] = 0
        # print(array)
        # sleep(1)
    else:
        counting2 = [0] * 101
        traversal2 = 1
        for rr in range(1, 101):
            if not G[rr][num]:
                continue
            else:
                temp2 = G[rr][num]
                counting2[temp2] += 1
                value2 = counting2[temp2]
                if value2 > traversal2:
                    traversal2 = value2
        array2 = []
        temp_row = 0
        tra2 = 1
        ele2 = 1
        while tra2 <= traversal2:
            if counting2[ele2] == tra2:
                array2.append(ele2)
                array2.append(tra2)
                temp_row += 2
                if temp_row == 100:
                    break
            if ele2 < 100:
                ele2 += 1
            else:
                tra2 += 1
                ele2 = 1
        if temp_row > mx_row:
            mx_row = temp_row
        for rrr in range(1, temp_row + 1):
            G[rrr][num] = array2[rrr - 1]
        for rrr in range(temp_row + 1, 101):
            G[rrr][num] = 0


G = [[0] * 102 for _ in range(102)]
r, c, k = map(int, input().split())
in_put = [list(map(int, input().split())) for _ in range(3)]
for R in range(3):
    for C in range(3):
        G[R + 1][C + 1] = in_put[R][C]
count = 0
mx_row = 3
mx_col = 3
while count <= 100:
    if G[r][c] == k:
        break
    elif mx_row >= mx_col:
        for rr in range(1, mx_row + 1):
            solve(1, rr)
    else:
        for cc in range(1, mx_col + 1):
            solve(0, cc)
    count += 1

if count > 100:
    print(-1)
else:
    print(count)
