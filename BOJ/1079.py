import sys

input = sys.stdin.readline


def solve(alive, dead, sins, night):
    global ans
    if dead[eunjin] or alive == 1:
        ans = max(ans, night)
    else:
        # 낮
        if alive % 2:
            mx_idx = 0
            mx_sin = 0
            for i in range(N):
                if not dead[i]:
                    sin = sins[i]
                    if sin > mx_sin:
                        mx_idx = i
                        mx_sin = sin
            # 죽이기
            dead[mx_idx] = True
            solve(alive - 1, dead, sins, night)
            dead[mx_idx] = False
        # 밤
        else:
            # 죽이고 점수 변환
            for i in range(N):
                if i != eunjin and not dead[i]:
                    dead[i] = True
                    for j in range(N):
                        if not dead[j]:
                            sins[j] += R[i][j]
                    solve(alive - 1, dead, sins, night + 1)
                    for j in range(N):
                        if not dead[j]:
                            sins[j] -= R[i][j]
                    dead[i] = False


def main():
    global N, R, eunjin
    N = int(input())
    sins = list(map(int, input().split()))
    R = [list(map(int, input().split())) for _ in range(N)]
    eunjin = int(input())

    dead = [False] * N
    alive = N
    solve(alive, dead, sins, 0)


if __name__ == "__main__":
    ans, N, eunjin = 0, 0, 0
    R = [[]]
    main()
    print(ans)
