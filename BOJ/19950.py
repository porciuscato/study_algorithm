import sys


input = sys.stdin.readline
x1, y1, z1, x2, y2, z2 = map(int, input().split())
N = int(input())
bars = list(map(int, input().split()))
distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2) ** 0.5
print(distance)