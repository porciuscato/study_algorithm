import sys
import math

input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    B, C = map(int, input().split())
    print(sum([1 if ele - B <= 0 else math.ceil((ele - B) / C) + 1 for ele in arr]))
