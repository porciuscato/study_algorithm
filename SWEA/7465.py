import sys

sys.stdin = open('input.txt', 'r')


for T in range(1, int(input()) + 1):
    ans = 0
    N, M = map(int, input().split())
    B = [[0] * N for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        B[a - 1][b - 1] = 1
        B[b - 1][a - 1] = 1
    v = [0] * N
    for i in range(N):
        if not v[i]:
            ans += 1
            st = [i]
            v[i] = 1
            while st:
                t = st.pop(-1)
                for j in range(N):
                    if not v[j] and B[t][j]:
                        v[j] = 1
                        st.append(j)
    print('#{} {}'.format(T, ans))