# 이 마저도 완전 탐색이 제대로 되지 않았다.
# DFS 형식으로 완점 탐색을 구현해야겠다.

from itertools import permutations
from heapq import heappop, heappush


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


def search(paper, checked, color_paper_left, sizes) -> int:
    answer = 0
    for size in sizes:
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


def main():
    global answers
    paper = [list(map(int, input().split())) for _ in range(10)]

    for permu in permutations((2, 3, 4, 5), 4):
        checked = [[False for _ in range(10)] for __ in range(10)]
        color_paper_left = [5, 5, 5, 5, 5]
        sizes = list(permu) + [1]
        heappush(answers, search(paper, checked, color_paper_left, sizes))


if __name__ == "__main__":
    answers = []
    main()
    while answers:
        answer = heappop(answers)
        if answer != -1:
            print(answer)
            break
    else:
        print(-1)


# 1 1 1 1 1 1 0 0 0 0
# 1 1 1 1 1 1 0 0 0 0
# 1 1 1 1 1 1 0 0 0 0
# 1 1 1 1 1 1 0 0 0 0
# 1 1 1 1 1 1 0 0 0 0
# 1 1 1 1 1 1 0 0 0 0
# 1 1 1 1 1 1 0 0 0 0
# 1 1 1 1 1 1 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0


# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 0 0 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 0 0 0 0