def solution(jobs):
    cont = len(jobs)
    jobs.sort(key=lambda x: (x[0], x[1]))
    visited = [False] * cont

    hard_now = 0
    total = 0
    for i in range(cont):
        hubo = []
        for j in range(cont):
            if not visited[j] and jobs[j][0] <= hard_now:
                hubo.append((jobs[j], j))
        if hubo:
            hubo.sort(key=lambda x: (x[0][1], x[0][0]))
            process = hubo[0]
            visited[process[1]] = True
            total += hard_now - process[0][0] + process[0][1]
            hard_now += process[0][1]
        else:
            for k in range(cont):
                if not visited[k]:
                    visited[k] = True
                    hard_now = sum(jobs[k])
                    total += jobs[k][1]
                    break
    return total // cont


cases = [
    [[0, 3], [1, 9], [2, 6]]
]

for case in cases:
    print(solution(case))
