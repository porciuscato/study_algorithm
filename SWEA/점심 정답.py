
def move(stair, arrival):
    if not arrival : return 0

    arrival.sort()
    tList = [0] * 200

    for t in arrival:
        h = S[stair][2]
        while h:
            t += 1
            if tList[t] < 3:
                tList[t] += 1
                h -= 1

    for i in range(199, 0, -1):
        if tList[i] : return i + 1


def f(state, pcnt):
    arrival0 = []
    arrival1 = []

    for i in range(pcnt):
        if state & (1 << i) == 0:
            arrival0.append(dist[i][0])
        else:
            arrival1.append(dist[i][1])

    return max(move(0, arrival0), move(1, arrival1))


for tc in range(1, int(input()) + 1):
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(N)]
    P = []
    S = []
    for i in range(N):
        for j in range(N):
            if m[i][j] == 1:
                P.append([i, j])
            elif m[i][j] != 0:
                S.append([i, j, m[i][j]])

    dist = [[0] * 2 for i in range(len(P))]
    for i in range(len(P)):
        dist[i][0] = abs(P[i][0] - S[0][0]) + abs(P[i][1] - S[0][1])
        dist[i][1] = abs(P[i][0] - S[1][0]) + abs(P[i][1] - S[1][1])

    ans = 10e9
    for state in range(1 << len(P)):  # 사람이 간 계단을 비트로 표시
        ans = min(ans, f(state, len(P)))

    print('#%d' % tc, ans)
