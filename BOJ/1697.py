if __name__ == "__main__":
    N, K = map(int, input().split())
    visited = [False] * 100001
    que = [(N, 0)]
    visited[N] = True
    answer = 0
    f = -1
    r = 0
    while que:
        f += 1
        pos, time = que[f]
        if pos == K:
            answer = time
            break
        for result in [pos - 1, pos + 1, pos * 2]:
            if 0 <= result <= 100000 and not visited[result]:
                visited[result] = True
                que.append((result, time + 1))
                r += 1
    print(answer)
