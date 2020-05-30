# def fibo(n, aim):
#     global answer
#     if n == 0:
#         answer[aim][0] += 1
#         return 0
#     elif n == 1:
#         answer[aim][1] += 1
#         return 1
#     else:
#         return fibo(n - 1, aim) + fibo(n - 2, aim)


answer = [[1, 0], [0, 1], [1, 1]]
answer += [[0, 0] for _ in range(38)]
for i in range(3, 41):
    answer[i][0] = answer[i - 1][1]
    answer[i][1] = answer[i - 1][0] + answer[i - 1][1]


for _ in range(int(input())):
    N = int(input())
    print('{} {}'.format(answer[N][0], answer[N][1]))
