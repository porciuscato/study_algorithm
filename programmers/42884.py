def solution(routes):
    routes.sort(key=lambda x: x[1])

    answer = 0
    camera = -100000
    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer


cases = [
    [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
]

for case in cases:
    print(solution(case))
