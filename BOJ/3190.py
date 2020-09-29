import sys
from collections import deque

input = sys.stdin.readline

delta = ((-1, 0), (0, 1), (1, 0), (0, -1))


def solve():
    time = 0
    worm = deque([(0, 0)])
    board[0][0][1] = 1
    direc = 1  # 위부터 시계 방향으로 0, 1, 2, 3
    mission = False
    while True:
        if not mission:
            try:
                m_time, m_direc = info.popleft()
            except IndexError:
                m_time, m_direc = -1, -1
            mission = True
        # 방향 전환
        if time == m_time:
            direc = (direc + m_direc) % 4
            mission = False
        # 이동
        newr = worm[0][0] + delta[direc][0]
        newc = worm[0][1] + delta[direc][1]
        if 0 <= newr < N and 0 <= newc < N:
            if board[newr][newc][1]:  # 몸에 부딪히면 끝
                time += 1
                break
            worm.appendleft((newr, newc))
            board[newr][newc][1] = 1
            if board[newr][newc][0]:  # 사과가 있다면
                board[newr][newc][0] = 0
            else:
                lastr, lastc = worm.pop()
                board[lastr][lastc][1] = 0
        else:
            time += 1
            break
        time += 1
    return time


if __name__ == "__main__":
    N = int(input())
    board = [[[0, 0] for _ in range(N)] for __ in range(N)]
    for _ in range(int(input())):
        ir, ic = map(lambda x: x - 1, map(int, input().split()))
        board[ir][ic][0] = 1
    info = deque([])
    for _ in range(int(input())):
        isec, idirec = input().split()
        if idirec == "L":
            idirec = -1
        else:
            idirec = 1
        info.append((int(isec), idirec))
    print(solve())
