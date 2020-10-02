import sys

input = sys.stdin.readline
delta = ((0, 0), (0, 1), (0, -1), (-1, 0), (1, 0))


class Dice:
    def __init__(self):
        self.status = [[-1, 0, -1],
                       [0, 0, 0],
                       [-1, 0, -1],
                       [-1, 0, -1]]

    def roll(self, direc):
        if direc == 3:  # 북
            temp = self.status[0][1]
            for i in range(3):
                self.status[i][1] = self.status[i + 1][1]
            self.status[3][1] = temp
        elif direc == 4:  # 남
            temp = self.status[3][1]
            for i in range(3, 0, -1):
                self.status[i][1] = self.status[i - 1][1]
            self.status[0][1] = temp
        elif direc == 1:  # 동
            right = self.status[1][2]
            bottom = self.status[3][1]
            for i in range(2, -1, -1):
                self.status[1][i] = self.status[1][i - 1]
            self.status[3][1] = right
            self.status[1][0] = bottom
        elif direc == 2:  # 서
            left = self.status[1][0]
            bottom = self.status[3][1]
            for i in range(2):
                self.status[1][i] = self.status[1][i + 1]
            self.status[3][1] = left
            self.status[1][2] = bottom

    def dice_print(self):
        print(self.status[1][1])

    def check_floor(self, row, col):
        if board[row][col] == 0:
            board[row][col] = self.status[3][1]
        else:
            self.status[3][1] = board[row][col]
            board[row][col] = 0


if __name__ == "__main__":
    N, M, x, y, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    orders = list(map(int, input().split()))
    dice = Dice()
    for order in orders:
        nr = x + delta[order][0]
        nc = y + delta[order][1]
        if 0 <= nr < N and 0 <= nc < M:
            dice.roll(order)
            dice.check_floor(nr, nc)
            dice.dice_print()
            x = nr
            y = nc
