import math


def solution(x, y, r, d, target):
    answer = 0
    # 원점과의 각도
    rad = math.atan2(y, x)
    value = rad * 180 / math.pi
    degree = value if value >= 0 else 360 + value

    radius = [degree - d, degree, degree, degree + d]
    if radius[3] >= 360:
        radius = [radius[0], 360, 0, radius[3] - 360]
    elif radius[0] < 0:
        radius = [radius[0] + 360, 360, 0, radius[3]]

    # 모든 점들과의 거리 및 각도
    for i in range(len(target)):
        mx = target[i][0]
        my = target[i][1]
        mrad = math.atan2(my, mx)
        mvalue = mrad * 180 / math.pi
        mdegree = mvalue if mvalue >= 0 else 360 + mvalue  # 각도
        mdistance = (mx ** 2 + my ** 2) ** 0.5  # 거리
        if mdistance <= r and (radius[0] <= mdegree < radius[1] or radius[2] <= mdegree <= radius[3]):
            answer += 1
    return answer


problems = [
    [-1, 2, 2, 60, [[0, 1], [-1, 1], [1, 0], [-2, 2]]]
]

for problem in problems:
    print(solution(*problem))
