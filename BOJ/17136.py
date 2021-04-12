# 그리디한 접근 방식으로 인해 엣지 케이스를 잡아내지 못했다.
# 완전탐색으로 코드를 재구성하자.


def is_color_paper_match(r: int, c: int, size: int, paper, checked) -> bool:
    for row in range(r, r + size):
        for col in range(c, c + size):
            if not paper[row][col] or checked[row][col]:
                return False
    return True


def check_paper(r, c, size, checked):
    for row in range(r, r + size):
        for col in range(c, c + size):
            checked[row][col] = True


def main() -> int:
    answer = 0
    paper = [list(map(int, input().split())) for _ in range(10)]
    checked = [[False for _ in range(10)] for __ in range(10)]
    color_paper_left = [5, 5, 5, 5, 5]

    for size in range(5, 0, -1):
        for r in range(10 - size + 1):
            for c in range(10 - size + 1):
                if paper[r][c] == 1 and not checked[r][c]:
                    if is_color_paper_match(r, c, size, paper, checked):
                        check_paper(r, c, size, checked)
                        answer += 1
                        color_paper_left[size - 1] -= 1
                        if color_paper_left[size - 1] < 0:
                            return -1
    return answer


if __name__ == "__main__":
    print(main())
