from collections import deque


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
        visited = [True] + [False for _ in range(N)]
        answers = []
        que = deque([])
        que.append((target, W[target]))
        DP[target] = W[target]
        while que:
            flag = True
            start, weight = que.popleft()
            for st in board[start]:
                if not visited[st] or board[st]:
                    value = DP[start] + W[st]
                    if value > DP[st]:
                        que.append((st, value))
                        DP[st] = value
                        flag = False
            if flag:
                answers.append(weight)
            else:
                visited[start] = True
        print(max(answers))


main()
