import sys

input = sys.stdin.readline
delta = ((-1, 0), (0, 1), (1, 0), (0, -1))


def rotate(p_red, p_blue, p_board, depth):
    global answer
    if depth > 10:
        return -1
    else:
        for rot in range(4):
            t_board = [[0] * N for _ in range(M)]
            for i in range(M):
                for j in range(N):
                    t_board[i][j] = p_board[i][j]
            # 두 구슬의 움직임을 만들어줘야....
            possible = True
            redr, redc = p_red
            bluer, bluec = p_blue
            while 1:
                if rot == 0:
                    pass
                elif rot == 1:
                    pass
                elif rot == 2:
                    pass
                elif rot == 3:
                    pass
                # 방향을 통해 밑에 있는 놈들 먼저 확인하자.
                # 그래서 밑에 있는 놈을 먼저 옮겨


                # 구멍에 들어가면
                # 어떻게 하지?
                # 일단 두 구슬의 좌표를 바꿔봐.
                # 그리고 확인하자.
                answer = min(answer, depth + 1)
                break

            # 움직임이 끝나면 board의 정보를 업데이트 시켜주자
            if possible:
                t_board[p_red[0]][p_red[1]] = "."
                t_board[p_blue[0]][p_blue[1]] = "."
                t_board[redr][redc] = "R"
                t_board[bluer][bluec] = "B"
                rotate([redr, redc], [bluer, bluec], t_board, depth + 1)
            else:
                continue


if __name__ == "__main__":
    N, M = map(int, input().split())
    blue = [0, 0]
    red = [0, 0]
    hole = [0, 0]
    board = []
    for i in range(M):
        board_row = list(input())
        for j in range(N):
            if board_row[j] == "O":
                hole = [i, j]
            elif board_row[j] == "R":
                red = [i, j]
            elif board_row[j] == "B":
                blue = [i, j]
        board.append(board_row)
    answer = 11
    result = rotate(red, blue, board, 0)
    print(result if not result else -1)
