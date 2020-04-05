# https://programmers.co.kr/learn/courses/30/lessons/43163


def solution(begin, target, words):
    words.insert(0, begin)
    word_len = len(begin)
    _len = len(words)
    DB = [[0] * _len for _ in range(_len)]
    # 전처리
    for i in range(_len):
        origin = words[i]
        for j in range(_len):
            if i == j:
                DB[i][j] = 1
            else:
                check = words[j]
                dif = 0
                for ch in range(word_len):
                    if origin[ch] != check[ch]:
                        dif += 1
                    if dif >= 2:
                        break
                if dif == 1:
                    DB[i][j] = 1
    # BFS 돌자
    visited = [0] * _len
    que = list()
    que.append((0, 0))
    while que:
        check, depth = que.pop(0)
        # print(words[check], depth)
        if words[check] == target:
            return depth
        for i in range(_len):
            if check != i and DB[check][i] and not visited[i]:
                que.append((i, depth + 1))
                visited[i] = 1
    return 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
