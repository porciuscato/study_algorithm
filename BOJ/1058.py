import sys
from collections import deque

input = sys.stdin.readline


def main():
    N = int(input())
    board = [input() for _ in range(N)]

    # BFS
    ans = 0
    for i in range(N):
        visited = [False] * N
        visited[i] = True
        que = deque([(i, 0)])
        temp_ans = 0
        while que:
            start, distance = que.popleft()
            for j in range(N):
                if distance < 2 and board[start][j] == 'Y' and not visited[j]:
                    temp_ans += 1
                    visited[j] = True
                    que.append((j, distance + 1))
        ans = max(ans, temp_ans)
    print(ans)


main()

# 6
# NNNYNN
# NNYNNY
# NYNYNN
# YNYNYN
# NNNYNN
# NYNNNN
# 5
#
# 5
# NYYNN
# YNYNN
# YYNYN
# NNYNY
# NNNYN
# 4
#
# 7
# NYNYYYY
# YNNNYNN
# NNNYNNN
# YNYNNNN
# YYNNNYY
# YNNNYNN
# YNNNYNN
# 6
#
# 2
# NN
# NN
# 0
#
# 2
# NY
# YN
# 1
#
# 1
# N
# 0
#
# 6
# NYYNYN
# YNYNNN
# YYNYNN
# NNYNNN
# YNNNNY
# NNNNYN
# 5

# 6
# NYNNNN
# YNYNNN
# NYNYNN
# NNYNNN
# NNNNNY
# NNNNYN
# 3

# 8
# NYNNNNNN
# YNYNNNNN
# NYNYNNNN
# NNYNNNYN
# NNNNNYNN
# NNNNYNNN
# NNNYNNNY
# NNNNNNYN
# 4