import sys

sys.stdin = open('14890.txt')


def execute(arr):
    global ANSWER
    chayi = [0] * N
    gyungsa = [0] * N
    need_to_make = 0

    # 차이 체크
    for idx in range(N - 1):
        chayi[idx] = arr[idx] - arr[idx + 1]
        chayi_value = chayi[idx]
        if chayi_value == 1 or chayi_value == -1:
            need_to_make += 1
        elif chayi_value > 1 or chayi_value < -1:
            return
    # 경사로 놓을 줄을 만들어
    for idx, val in enumerate(chayi):
        # -1 이면 본인부터 왼쪽으로 확인
        check_idx_list = []
        if val == -1:
            check_idx_list = [n for n in range(idx + 1 - L, idx + 1)]
        # 1 이면 그 다음부터 오른쪽으로 확인
        elif val == 1:
            check_idx_list = [n for n in range(idx + 1, idx + 1 + L)]
        # check_idx_list 가 모두 범위에 있는가?
        if check_idx_list and check_idx_list[0] >= 0 and check_idx_list[-1] < N:
            # 모두 같은 값인가?
            check_value = arr[check_idx_list[0]]
            for check_idx in check_idx_list:
                if check_value != arr[check_idx]:
                    break
            else:
                for check_idx in check_idx_list:
                    # 모든 gyunsa가 0인가?
                    if gyungsa[check_idx] == 1:
                        break
                else:
                    # 모두 충족하면 need_to_make -= 1
                    for check_idx in check_idx_list:
                        gyungsa[check_idx] = 1
                    need_to_make -= 1
        else:
            continue

    # 다 끝나고 need 가 0이면 ans +=1
    if need_to_make == 0:
        ANSWER += 1


N, L = map(int, input().split())
TABLE = [list(map(int, input().split())) for _ in range(N)]
ANSWER = 0
# 가로줄 확인
for row in range(N):
    origin = TABLE[row]
    execute(origin)
# 세로 확인
for col in range(N):
    origin = [TABLE[row][col] for row in range(N)]
    execute(origin)
print(ANSWER)