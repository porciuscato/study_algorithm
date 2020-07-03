from collections import deque
import sys

input = sys.stdin.readline


def main():
    for t in range(int(input())):
        # input
        N, K = map(int, input().split())
        W = [0] + list(map(int, input().split()))
        board = [[] for __ in range(N + 1)]
        for k in range(K):
            s, e = map(int, input().split())
            board[e].append(s)
        target = int(input())

        # BFS
        DP = [0 for _ in range(N + 1)]
        que = deque([])
        que.append((target, W[target]))
        DP[target] = W[target]
        while que:
            start, weight = que.popleft()
            for st in board[start]:
                value = DP[start] + W[st]
                if value > DP[st]:
                    DP[st] = value
                    if board[st]:
                        que.append((st, value))
        print(max(DP))


main()