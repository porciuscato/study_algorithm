import sys

sys.stdin = open('5653.txt', 'r')


for T in range(1, int(input()) + 1):
    # 비활성, 활성 세포들을 여기서 관리 / 크기에 따라 10개의 공간을 만들어 놓음
    cells = [[], [], [], [], [], [], [], [], [], []]
    N, M, K = map(int, input().split())
    TABLE = [[0] * 351 for _ in range(351)]
    # 세포들의 수
    count = 0
    for r in range(N):
        t = list(map(int, input().split()))
        for c in range(M):
            if t[c]:
                big = t[c]
                # 좌표 + 150
                TABLE[r + 150][c + 150] = big  # 상태: 0 죽음, 1 활성, 2 비활성
                # row, col, 수명, 상태, 남은시간
                cells[big - 1].append([r + 150, c + 150, big, 2, big])  # 크기에 따라 넣는 위치를 달리함
                count += 1

    k = 0
    while k < K:
        # 큰 세포들부터 번식
        for cell_size in range(9, -1, -1):
            if cells[cell_size]:
                length = len(cells[cell_size])
                # 죽은 세포의 인덱스를 저장
                dead_cells = []
                for idx in range(length):
                    data = cells[cell_size][idx]
                    # 상태에 따라 다르게 처리한다.
                    if data[3] == 2:  # 비활성
                        # 비활성 상태라면 남은 시간을 1 줄여준다.
                        data[4] -= 1
                        # 남은 시간이 0이 되면 상태를 1로 바꾸고 남은 시간을 다시 수명만큼 바꾼다.
                        if data[4] == 0:
                            data[3] = 1
                            data[4] = data[2]
                    elif data[3] == 1:  # 활성
                        # 세포 증식을 한다. 증식의 표시는 TABLE에 한다. TABLE에 무언가 다른 수가 있으면 증식을 하지 않는다.
                        row = data[0]
                        col = data[1]
                        life = data[2]
                        for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                            drow = row + dr
                            dcol = col + dc
                            if not TABLE[drow][dcol]:
                                # 새로 생긴 세포는 cells에 포함시키고 count += 1
                                TABLE[drow][dcol] = life
                                cells[cell_size].append([drow, dcol, life, 2, life])
                                count += 1
                        # 끝나면 시간을 1 줄인다. 남은 시간이 0 되면 dead_cells에 인덱스를 저장한다.
                        data[4] -= 1
                        if data[4] == 0:
                            dead_cells.append(idx)
                # dead_cells를 뒤에서부터 돌며 죽은 세포들을 뺀다.
                for dead in dead_cells[::-1]:
                    cells[cell_size].pop(dead)
                    count -= 1
        k += 1
    print('#{} {}'.format(T, count))
